
-- This sets up the "standard" run we use in the unit tests, you can then
-- use this and override any feature you want to be done differently
--
-- Pull anything from CommonConfig through the CommonConfig name and
-- anything in OcoConfig from that name instead of all through OcoConfig
-- to better differentiate where routines are being loaded from.

require "oco_config"
oco_base_config_dir = ConfigCommon.local_dir()

OcoBaseConfig = OcoConfig:new {
------------------------------------------------------------
--- Various constants used to describe input data.
------------------------------------------------------------

   -- As a convenience, we pass in a few fields by environment
   -- variables.
   sid_string = os.getenv("sounding_id"),
   spectrum_file = os.getenv("spectrum_file"),
   met_file = os.getenv("met_file"),
   imap_file = os.getenv("imap_file"),
   --- Scene file is only used it we are trying to match a simulator
   --- run. So for a real data, this will be a empty string, and will
   --- in fact be ignored.
   scene_file = os.getenv("scene_file"),
   static_file = oco_base_config_dir .. "/../input/l2_oco_static_input.h5",
   static_eof_file = oco_base_config_dir .. "/../input/l2_oco_eof.h5",
   static_solar_file = config_common_dir .. "/../input/l2_solar_model.h5",
   static_aerosol_file = config_common_dir .. "/../input/l2_aerosol_combined.h5",
   -- Can have a different aerosol file for Merra aerosols
   -- static_merra_aerosol_file = config_common_dir .. "/../input/l2_aerosol_combined_RH.h5",

   merra_dir = "/groups/algorithm/l2_fp/merra_composite",

------------------------------------------------------------
-- Set this true to get diagnostic messages to help debug
-- problems with Lua
------------------------------------------------------------

   diagnostic = false,

------------------------------------------------------------
-- Paths for Absco data. We first look in local path, and if
-- we can't read the file try the full path. This allows us
-- to use a local disk on the cluster.
------------------------------------------------------------

   absco_local_path = "/state/partition1/groups/algorithm/l2_fp/absco",
   absco_path = "/groups/algorithm/l2_fp/absco",

------------------------------------------------------------
-- Connor solver
------------------------------------------------------------

   solver = { threshold=2.0,
              min_iteration=1,
              max_iteration=7,
              max_divergence=2,
              max_chisq=1.4,
              gamma_initial=10.0,
              h2o_scale_index0=-20,
              h2o_scale_index1=-20,
              h2o_scale_cov_initial=0.001,
              ch4_scale_index0=-21,
              ch4_scale_index1=-21,
              ch4_scale_cov_initial=0.001,
              co_scale_index0=-22,
              co_scale_index1=-22,
              co_scale_cov_initial=0.0001,
              create = ConfigCommon.connor_solver,
            },

------------------------------------------------------------
-- Iterative solver
--
-- Thresholds and limits for the retrieval process.  
-- Some thresholds are for testing the cost function.  For
-- example g_tol_abs is a tolerance for checking the 
-- gradient of the cost function.  On the other hand, some
-- are used for testing the minimizer (solver).  For
-- example, minimizer_size_tol is used to check the solver.
-- Therefore, we cal this group of constants the retrieval
-- thresholds and not the solver or the problem thresholds.
------------------------------------------------------------

   -- solver = 
   not_used_solver = { max_cost_function_calls=20,
                       dx_tol_abs=1e-5,
                       dx_tol_rel=1e-5,
                       g_tol_abs=1e-5,
                       minimizer_size_tol=1e-5,
                       opt_problem = ConfigCommon.nlls_max_a_posteriori,
                       iter_solver = ConfigCommon.nlls_solver_gsl_lmsder,
                       create = ConfigCommon.iterative_solver},

------------------------------------------------------------
-- If true then launch solver, otherwise just do a 
-- forward model calculation, with jacobians if
-- write_jacobians is true
------------------------------------------------------------

   do_retrieval = true,

------------------------------------------------------------
-- True if we want to write the jacobians out
------------------------------------------------------------

   write_jacobian = false,

------------------------------------------------------------
-- True if we want to write high resolution spectra out
------------------------------------------------------------

   write_high_res_spectra = false,

------------------------------------------------------------
-- True if we want to generate output for every iteration
------------------------------------------------------------

   iteration_output = false,

------------------------------------------------------------
--- Log level
------------------------------------------------------------

   log_level = LogImp.INFO,

-----------------------------------------------------------
--- Default creators for everything. We default to getting stuff
--- from the HDF file, but this can be changed if desired.
------------------------------------------------------------

   fm = {
      creator = ConfigCommon.oco_forward_model,
      common = {
         desc_band_name = ConfigCommon.hdf_read_string_vector("Common/desc_band_name"),
         hdf_band_name = ConfigCommon.hdf_read_string_vector("Common/hdf_band_name"),
         band_reference = ConfigCommon.hdf_read_double_with_unit_1d("Common/band_reference_point"),
         creator = ConfigCommon.table_function_eval,
      },
      spec_win = {
         creator = ConfigCommon.spectral_window_hdf,
         bad_sample_mask = OcoConfig.bad_sample_mask_with_saa,
         bad_sample_mask_before_saa = OcoConfig.l1b_bad_sample_mask,
         latitude_min = -50,
         latitude_max = 0,
         longitude_min = -90,
         longitude_max = 10,
         saa_tolerance = 6,
      },
      input = {
         creator = ConfigCommon.l1b_met_input,
         l1b = {
            creator = OcoConfig.level1b_hdf,
            noise = {
               creator = OcoConfig.oco_noise,
               max_ms = { 7.00e20, 2.45e20, 1.25e20 },
            },
            --- Can select this to include bad samples in residual, with a
            --- really high uncertainty. Should also remove bad_sample from
            --- the spectral window if you use this (so 
            --- config.fm.spec_win.bad_sample_mask = nil. Should also set
            --- spectral window to be the full range.
            -- noise = {
            --    bad_sample_mask = OcoConfig.bad_sample_mask_outside_window,
            --    bad_sample_mask_before_window = OcoConfig.bad_sample_mask_with_saa,
            --    bad_sample_mask_before_saa = OcoConfig.snr_coef_bad_sample_mask,
            --    latitude_min = -50,
            --    latitude_max = 0,
            --    longitude_min = -90,
            --    longitude_max = 10,
            --    saa_tolerance = 6,
            --    bad_sample_uncertainty = 1e24,
            --    creator = OcoConfig.bad_sample_noise_model,
            --    creator_before_bad_sample = OcoConfig.oco_noise,
            --    max_ms = { 7.00e20, 2.45e20, 1.25e20 },
            -- },
         },
         met = {
            creator = OcoConfig.oco_met,
         },
      },
      stokes_coefficient = {
         creator = ConfigCommon.stokes_coefficient_constant,
         value = ConfigCommon.stokes_coefficient_l1b,
         -- Hard code value rather than reading from l1b
         -- value = ConfigCommon.stokes_coefficient_value({{1,2,3,4},{5,6,7,8},{9,10,11,12}}),
      },
      instrument = {
         creator = ConfigCommon.ils_instrument,
         ils_half_width = { DoubleWithUnit(4.09e-04, "um"), 
                            DoubleWithUnit(1.08e-03, "um"),
                            DoubleWithUnit(1.40e-03, "um") },
         dispersion = {
            creator = ConfigCommon.dispersion_polynomial,
            apriori = ConfigCommon.l1b_spectral_coefficient_i,
            covariance = OcoConfig.dispersion_covariance_i("Instrument/Dispersion"),
            number_pixel = ConfigCommon.hdf_read_int_1d("Instrument/Dispersion/number_pixel"),
            retrieved = true,
            is_one_based = true,
            num_parameters = 2,
         },
         ils_func = {
            creator = OcoConfig.ils_table_l1b,
         },
         instrument_correction = {
            creator = OcoConfig.instrument_correction_list_acquisition_mode,
            -- Right now we are using only one set of EOFs for all 3 modes.
            -- If we end up doing this all the time in the future, we should
            -- consider just adding a new creator that doesn't pick the EOF
            -- base on mode. But for now leave this functionality in.
            ic_nadir = { "eof_glint_1", "eof_glint_2","eof_glint_3",},
            ic_glint = { "eof_glint_1", "eof_glint_2","eof_glint_3",},
            ic_target = { "eof_glint_1", "eof_glint_2","eof_glint_3",},
            --ic_nadir = { "eof_nadir_1", "eof_nadir_2", "eof_nadir_3",},
            --ic_glint = { "eof_glint_1", "eof_glint_2", "eof_glint_3",},
            --ic_target = { "eof_target_1", "eof_target_2", "eof_target_3",},
            eof_nadir_1 = {
               hdf_group = "Instrument/EmpiricalOrthogonalFunction/Nadir",
               apriori = ConfigCommon.hdf_eof_apriori_i_j("Instrument/EmpiricalOrthogonalFunction", 1 - 1),
               covariance = ConfigCommon.hdf_eof_covariance_i_j("Instrument/EmpiricalOrthogonalFunction", 1 - 1),
               order = 1,
               by_pixel = true,
	       scale_uncertainty = true,
	       scale_to_stddev = 1e19,
               creator = ConfigCommon.empirical_orthogonal_function,
               retrieve_bands = { true, true, true },
	       eof_used = {true, true, true},
            },
            eof_nadir_2 = {
               hdf_group = "Instrument/EmpiricalOrthogonalFunction/Nadir",
               apriori = ConfigCommon.hdf_eof_apriori_i_j("Instrument/EmpiricalOrthogonalFunction", 2 - 1),
               covariance = ConfigCommon.hdf_eof_covariance_i_j("Instrument/EmpiricalOrthogonalFunction", 2 - 1),
               order = 2,
               by_pixel = true,
	       scale_uncertainty = true,
	       scale_to_stddev = 1e19,
               creator = ConfigCommon.empirical_orthogonal_function,
               retrieve_bands = { true, true, true },
	       eof_used = {true, true, true},
            },
            eof_nadir_3 = {
               hdf_group = "Instrument/EmpiricalOrthogonalFunction/Nadir",
               apriori = ConfigCommon.hdf_eof_apriori_i_j("Instrument/EmpiricalOrthogonalFunction", 3 - 1),
               covariance = ConfigCommon.hdf_eof_covariance_i_j("Instrument/EmpiricalOrthogonalFunction", 3 - 1),
               order = 3,
               by_pixel = true,
	       scale_uncertainty = true,
	       scale_to_stddev = 1e19,
               creator = ConfigCommon.empirical_orthogonal_function,
               retrieve_bands = { true, true, true },
	       eof_used = {true, true, true},
            },
            eof_glint_1 = {
               hdf_group = "Instrument/EmpiricalOrthogonalFunction/Glint",
               apriori = ConfigCommon.hdf_eof_apriori_i_j("Instrument/EmpiricalOrthogonalFunction", 1 - 1),
               covariance = ConfigCommon.hdf_eof_covariance_i_j("Instrument/EmpiricalOrthogonalFunction", 1 - 1),
               order = 1,
               by_pixel = true,
	       scale_uncertainty = true,
	       scale_to_stddev = 1e19,
               creator = ConfigCommon.empirical_orthogonal_function,
               retrieve_bands = { true, true, true },
	       eof_used = {true, true, true},
            },
            eof_glint_2 = {
               hdf_group = "Instrument/EmpiricalOrthogonalFunction/Glint",
               apriori = ConfigCommon.hdf_eof_apriori_i_j("Instrument/EmpiricalOrthogonalFunction", 2 - 1),
               covariance = ConfigCommon.hdf_eof_covariance_i_j("Instrument/EmpiricalOrthogonalFunction", 2 - 1),
               order = 2,
               by_pixel = true,
	       scale_uncertainty = true,
	       scale_to_stddev = 1e19,
               creator = ConfigCommon.empirical_orthogonal_function,
               retrieve_bands = { true, true, true },
	       eof_used = {true, true, true},
            },
            eof_glint_3 = {
               hdf_group = "Instrument/EmpiricalOrthogonalFunction/Glint",
               apriori = ConfigCommon.hdf_eof_apriori_i_j("Instrument/EmpiricalOrthogonalFunction", 3 - 1),
               covariance = ConfigCommon.hdf_eof_covariance_i_j("Instrument/EmpiricalOrthogonalFunction", 3 - 1),
               order = 3,
               by_pixel = true,
	       scale_uncertainty = true,
	       scale_to_stddev = 1e19,
               creator = ConfigCommon.empirical_orthogonal_function,
               retrieve_bands = { true, true, true },
	       eof_used = {true, true, true},
            },
            eof_glint_4 = {
               hdf_group = "Instrument/EmpiricalOrthogonalFunction/Glint",
               apriori = ConfigCommon.hdf_eof_apriori_i_j("Instrument/EmpiricalOrthogonalFunction", 4 - 1),
               covariance = ConfigCommon.hdf_eof_covariance_i_j("Instrument/EmpiricalOrthogonalFunction", 4 - 1),
               order = 4,
               by_pixel = true,
               scale_uncertainty = true,
               scale_to_stddev = 1e19,
               creator = ConfigCommon.empirical_orthogonal_function,
               retrieve_bands = { true, true, true },
	       eof_used = {true, true, true},
            },
            eof_target_1 = {
               hdf_group = "Instrument/EmpiricalOrthogonalFunction/Target",
               apriori = ConfigCommon.hdf_eof_apriori_i_j("Instrument/EmpiricalOrthogonalFunction", 1 - 1),
               covariance = ConfigCommon.hdf_eof_covariance_i_j("Instrument/EmpiricalOrthogonalFunction", 1 - 1),
               order = 1,
               by_pixel = true,
	       scale_uncertainty = true,
	       scale_to_stddev = 1e19,
               creator = ConfigCommon.empirical_orthogonal_function,
               retrieve_bands = { true, true, true },
	       eof_used = {true, true, true},
            },
            eof_target_2 = {
               hdf_group = "Instrument/EmpiricalOrthogonalFunction/Target",
               apriori = ConfigCommon.hdf_eof_apriori_i_j("Instrument/EmpiricalOrthogonalFunction", 2 - 1),
               covariance = ConfigCommon.hdf_eof_covariance_i_j("Instrument/EmpiricalOrthogonalFunction", 2 - 1),
               order = 2,
               by_pixel = true,
	       scale_uncertainty = true,
	       scale_to_stddev = 1e19,
               creator = ConfigCommon.empirical_orthogonal_function,
               retrieve_bands = { true, true, true },
	       eof_used = {true, true, true},
            },
            eof_target_3 = {
               hdf_group = "Instrument/EmpiricalOrthogonalFunction/Target",
               apriori = ConfigCommon.hdf_eof_apriori_i_j("Instrument/EmpiricalOrthogonalFunction", 3 - 1),
               covariance = ConfigCommon.hdf_eof_covariance_i_j("Instrument/EmpiricalOrthogonalFunction", 3 - 1),
               order = 3,
               by_pixel = true,
	       scale_uncertainty = true,
	       scale_to_stddev = 1e19,
               creator = ConfigCommon.empirical_orthogonal_function,
               retrieve_bands = { true, true, true },
	       eof_used = {true, true, true},
            },

            -- Disabled by default, add "radiance_scaling" to 
            -- config.fm.instrument_correction.ic to enable.
            -- Coxmunk+Lambertian will be used instead
            radiance_scaling = {
               apriori = ConfigCommon.hdf_apriori_i("Instrument/RadianceScaling/Coxmunk"),
               covariance = ConfigCommon.hdf_covariance_i("Instrument/RadianceScaling/Coxmunk"),
               creator = ConfigCommon.radiance_scaling_sv_fit_coxmunk_only,
               retrieve_bands = { true, true, true },
            },
         },
      },
      spectrum_effect = {
         creator = ConfigCommon.spectrum_effect_list,
         speceff = { "solar_model", "instrument_doppler", "fluorescence" },
         solar_model = {
            creator = ConfigCommon.solar_absorption_and_continuum,
            doppler_shift = {
               creator = ConfigCommon.solar_doppler_from_l1b,
               do_doppler_shift = true,
            },
            solar_absorption = {
               creator = ConfigCommon.solar_absorption_table,
            },
            solar_continuum = {
               creator = ConfigCommon.solar_continuum_table,
               convert_from_photon = false,
            },
         },
         instrument_doppler = {
            creator = ConfigCommon.instrument_doppler,
            retrieved = false,
         },
         fluorescence = {
            apriori = ConfigCommon.fluorescence_apriori("Fluorescence"),
            sif_sigma_scale = 1.0 / 3,
            covariance = ConfigCommon.fluorescence_covariance("Fluorescence"),
            creator = OcoConfig.fluorescence_effect_land_only,
            reference_point = ConfigCommon.hdf_read_double_with_unit("Fluorescence/reference_point"),
            retrieved = true,
         },
      },
      spec_samp = {
--       creator = ConfigCommon.uniform_spectrum_sampling,
         creator = ConfigCommon.nonuniform_spectrum_sampling,
         high_resolution_spectrum_spacing = DoubleWithUnit(0.01, "cm^-1"),
         nonunif_rt_grid_files = { 
            o2 = ConfigCommon.hdf_read_spec_dom("Spectrum_Sampling/nonuniform_grid_1"),
            weak_co2 = ConfigCommon.hdf_read_spec_dom("Spectrum_Sampling/nonuniform_grid_2"),
            strong_co2 = ConfigCommon.hdf_read_spec_dom("Spectrum_Sampling/nonuniform_grid_3"),
         },
      },
      rt = {
         creator = ConfigCommon.radiative_transfer_lsi,
         nadir_threshold = 1e-6,
         lsi_constant = {
            dedicated_twostream = true,
	    -- Note that the "1" here is just a convention to use the
	    -- dedicated two stream code
            low_stream = 1,
	    -- LIDORT input is in Half-Streams. Full-streams is double
	    -- this (so high_stream = 8 would mean 16 full-streams)
            high_stream = 8
         },
      },
      state_vector = {
         creator = ConfigCommon.state_vector_creator,
      },
      atmosphere = {
         creator = ConfigCommon.atmosphere_oco,
         constants = {
            creator = ConfigCommon.default_constant,
         },
         pressure = {
            apriori = ConfigCommon.met_pressure,
            covariance = ConfigCommon.hdf_covariance("Surface_Pressure"),
            a = ConfigCommon.hdf_read_double_1d("Pressure/Pressure_sigma_a"),
            b = ConfigCommon.hdf_read_double_1d("Pressure/Pressure_sigma_b"),
            creator = ConfigCommon.pressure_sigma,
         },
         temperature = {
            apriori = ConfigCommon.hdf_apriori("Temperature/Offset"),
            covariance = ConfigCommon.hdf_covariance("Temperature/Offset"),
            creator = ConfigCommon.temperature_met,
         },
         ground = {
            -- Instrument specific solar strengths used for ground calculations 
            solar_strength = {4.87e21, 2.096e21, 1.15e21},

            -- Pure lambertian
            lambertian = {
               apriori = OcoConfig.oco_albedo_from_radiance(1),  
               covariance = ConfigCommon.hdf_covariance_i("Ground/Albedo"),
               retrieve_bands = { true, true, true },
               creator = ConfigCommon.lambertian_retrieval,
            },

            -- Coxmunk windspeed and refractive index inputs
            coxmunk = {
               refractive_index = ConfigCommon.hdf_apriori("Ground/Refractive_Index"),
               apriori = ConfigCommon.met_windspeed,
               covariance = ConfigCommon.hdf_covariance("Ground/Windspeed"),
               creator = ConfigCommon.coxmunk_retrieval,
            },

            -- Lambertian component of coxmunk + lambertian
            coxmunk_lambertian = {
               apriori = ConfigCommon.hdf_apriori_i("Ground/Coxmunk_Albedo"),
               covariance = ConfigCommon.hdf_covariance_i("Ground/Coxmunk_Albedo"),
               retrieve_bands = { true, true, true },
               creator = ConfigCommon.lambertian_retrieval,
            },

            -- Brdf vegetative kernel with Rahman retrieved parameters
            brdf_veg = {
               apriori = ConfigCommon.brdf_veg_apriori("Ground/Brdf"),
               covariance = ConfigCommon.hdf_covariance_i("Ground/Brdf"),
               retrieve_bands = { true, true, true },
               creator = ConfigCommon.brdf_veg_retrieval,
            },
            
            -- Brdf soil kernel with Rahman retrieved parameters
            brdf_soil = {
               apriori = ConfigCommon.brdf_soil_apriori("Ground/Brdf"),
               covariance = ConfigCommon.hdf_covariance_i("Ground/Brdf"),
               retrieve_bands = { true, true, true },
               creator = ConfigCommon.brdf_soil_retrieval,
            },

            creator = OcoConfig.ground_from_ground_type,
         },
         aerosol = {
            creator = ConfigCommon.merra_aerosol_creator,
            max_aod = 0.2,
            exp_aod = 0.8,
            min_types = 2,
            max_types = 2,
	    linear_aod = false,
	    relative_humidity_aerosol = false,
            max_residual = 0.005,
            apriori = ConfigCommon.hdf_apriori("/Aerosol/Merra/Gaussian/Log"),
            covariance = ConfigCommon.hdf_covariance("/Aerosol/Merra/Gaussian/Log"),
            -- Lua doesn't preserve order in a table, so we have a list
            -- saying what order we want the Aerosols in
            aerosols = {"Ice", "Water", "ST"},
            Water = {
               creator = ConfigCommon.aerosol_log_shape_gaussian,
               apriori = ConfigCommon.hdf_aerosol_apriori("Aerosol", "Gaussian/Log"),
               covariance = ConfigCommon.hdf_aerosol_covariance("Aerosol", "Gaussian/Log"),
               property = ConfigCommon.hdf_aerosol_property("wc_008"),
            },
            Ice = {
               creator = ConfigCommon.aerosol_log_shape_gaussian,
               apriori_initial = ConfigCommon.hdf_aerosol_apriori("Aerosol", "Gaussian/Log"),
	       apriori = OcoConfig.tropopause_height_ap,
               covariance = ConfigCommon.hdf_aerosol_covariance("Aerosol", "Gaussian/Log"),
               property = ConfigCommon.hdf_aerosol_property("ice_cloud_MODIS6_deltaM_1000"),
            },
	    ST = {
	       creator = ConfigCommon.aerosol_log_shape_gaussian,
	       apriori = function(self)
		  return ConfigCommon.lua_to_blitz_double_1d({-5.11599580975408205124,0.03,0.04})
	       end,
	       covariance = function(self)
		  return ConfigCommon.lua_to_blitz_double_2d({{3.24,0,0},{0,1e-8,0},{0,0,1e-4}})
	       end,
	       property = ConfigCommon.hdf_aerosol_property("strat"),
	    },
         },
         absorber = {
            creator = ConfigCommon.absorber_creator,
            gases = {"CO2", "H2O", "O2"},
            CO2 = {
               apriori = ConfigCommon.reference_co2_apriori_met_apriori,
               covariance = ConfigCommon.hdf_covariance("Gas/CO2"),
               absco = "v5.0_alpha/raw/co2_devi2015_wco2scale=nist_sco2scale=unity.hdf",
               table_scale = {1.0, 1.0, 1.004},
               creator = ConfigCommon.vmr_level,
            },
            H2O = {
               scale_apriori = 1.0,
               scale_cov = 0.25,
               absco = "v5.0_alpha/raw/h2o_hitran12.h5",
               creator = ConfigCommon.vmr_met,
            },
            O2 = {
               apriori = ConfigCommon.hdf_read_double_1d("Gas/O2/average_mole_fraction"),
               absco = "v5.0_alpha/raw/o2_v151005_cia_mlawer_v151005r1_narrow.hdf",
               table_scale = 1.0,
               creator = ConfigCommon.vmr_level_constant_well_mixed,
            },
         },
         altitude = {
            creator = ConfigCommon.hydrostatic_altitude,
         },
	 relative_humidity = {
	    creator = ConfigCommon.calc_relative_humidity,
	 },
      },
   },
}
