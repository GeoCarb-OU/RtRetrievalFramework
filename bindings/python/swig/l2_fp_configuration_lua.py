# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _l2_fp_configuration_lua.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_l2_fp_configuration_lua', [dirname(__file__)])
        except ImportError:
            import _l2_fp_configuration_lua
            return _l2_fp_configuration_lua
        if fp is not None:
            try:
                _mod = imp.load_module('_l2_fp_configuration_lua', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _l2_fp_configuration_lua = swig_import_helper()
    del swig_import_helper
else:
    import _l2_fp_configuration_lua
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x



_l2_fp_configuration_lua.SHARED_PTR_DISOWN_swigconstant(_l2_fp_configuration_lua)
SHARED_PTR_DISOWN = _l2_fp_configuration_lua.SHARED_PTR_DISOWN

def _new_from_init(cls, version, *args):
    '''For use with pickle, covers common case where we just store the
    arguments needed to create an object. See for example HdfFile'''
    if(cls.pickle_format_version() != version):
      raise RuntimeException("Class is expecting a pickled object with version number %d, but we found %d" % (cls.pickle_format_version(), version))
    inst = cls.__new__(cls)
    inst.__init__(*args)
    return inst

def _new_from_set(cls, version, *args):
    '''For use with pickle, covers common case where we use a set function 
    to assign the value'''
    if(cls.pickle_format_version() != version):
      raise RuntimeException("Class is expecting a pickled object with version number %d, but we found %d" % (cls.pickle_format_version(), version))
    inst = cls.__new__(cls)
    inst.__init__()
    inst.set(*args)
    return inst

import full_physics_swig.l2_fp_configuration
import full_physics_swig.generic_object
class L2FpConfigurationLua(full_physics_swig.l2_fp_configuration.L2FpConfiguration):
    """

    This is an implementation of L2FpConfiguration that uses Lua.

    Note that this class is very specific to the L2 Full Physics main,
    with a minimal interface. A more general class LuaFile may be of more
    interest to you unless you are specifically working with L2 main.

    The interface is purposely minimal, there are a handleful of global
    variables that the Lua file need to define. It can do this in any way
    it wishes.

    In practice, our runs tend to be similiar. There is a file
    config_common.lua and base_config.lua that sets up a "standard" run,
    you can then create a configuration file that uses these two other
    files and just specifies what is different from this. But this is
    merely meant for convience, there is no requirement at all that you
    use these files. You can do anything you like as long as in the end
    you produce the set of global variables.

    The require variables are:

    logger - A LogImp

    forward_model - A ForwardModel

    solver - A ConnorSolver

    initial_guess - A InitialGuess

    number_pressure_level - Integer giving the number of pressure levels.
    This is used to size the output file, so it should be the maximim
    pressure

    number_aerosol - Integer giving number of Aerosol particles. Can be 0.
    This is used to size the output file.

    iteration_output - Boolean. True if we should write out iteration
    output

    register_output - A std::vector<boost::shared_ptr<RegisterOutputBase>
    > giving the list of output that should be generated. This list can
    empty if no output is desired. The Lua type for this is called
    VectorRegisterOutput (since Lua doesn't have templates).

    C++ includes: l2_fp_configuration_lua.h 
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """

        FullPhysics::L2FpConfigurationLua::L2FpConfigurationLua(int Argc, char **Argv)
        Parse the arguments passed to the executable to set up configuration.

        """
        _l2_fp_configuration_lua.L2FpConfigurationLua_swiginit(self, _l2_fp_configuration_lua.new_L2FpConfigurationLua(*args))

    def _v_lua_state(self):
        """

        LuaState& FullPhysics::L2FpConfigurationLua::lua_state()

        """
        return _l2_fp_configuration_lua.L2FpConfigurationLua__v_lua_state(self)


    @property
    def lua_state(self):
        return self._v_lua_state()


    def _v_output_name(self, *args):
        """

        void FullPhysics::L2FpConfigurationLua::output_name(const std::string &F)

        """
        return _l2_fp_configuration_lua.L2FpConfigurationLua__v_output_name(self, *args)


    @property
    def output_name(self):
        return self._v_output_name()

    @output_name.setter
    def output_name(self, value):
      self._v_output_name(value)

    __swig_destroy__ = _l2_fp_configuration_lua.delete_L2FpConfigurationLua
L2FpConfigurationLua._v_lua_state = new_instancemethod(_l2_fp_configuration_lua.L2FpConfigurationLua__v_lua_state, None, L2FpConfigurationLua)
L2FpConfigurationLua._v_output_name = new_instancemethod(_l2_fp_configuration_lua.L2FpConfigurationLua__v_output_name, None, L2FpConfigurationLua)
L2FpConfigurationLua_swigregister = _l2_fp_configuration_lua.L2FpConfigurationLua_swigregister
L2FpConfigurationLua_swigregister(L2FpConfigurationLua)



