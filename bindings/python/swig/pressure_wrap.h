/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 3.0.7
 *
 * This file is not intended to be easily readable and contains a number of
 * coding conventions designed to improve portability and efficiency. Do not make
 * changes to this file unless you know what you are doing--modify the SWIG
 * interface file instead.
 * ----------------------------------------------------------------------------- */

#ifndef SWIG_pressure_WRAP_H_
#define SWIG_pressure_WRAP_H_

#include <map>
#include <string>


class SwigDirector_Pressure : public FullPhysics::Pressure, public Swig::Director {

public:
    SwigDirector_Pressure(PyObject *self);
    virtual ~SwigDirector_Pressure();
    virtual void notify_add(FullPhysics::StateVector &Obs);
    virtual void notify_remove(FullPhysics::StateVector &Obs);
    virtual void notify_update(FullPhysics::StateVector const &Obs);
    virtual void mark_used(FullPhysics::StateVector const &Sv, blitz::Array< bool,1 > &Used) const;
    virtual void state_vector_name(FullPhysics::StateVector const &Sv, blitz::Array< std::string,1 > &Sv_name) const;
    virtual void add_observer(FullPhysics::Observer< FullPhysics::Pressure > &Obs);
    virtual void remove_observer(FullPhysics::Observer< FullPhysics::Pressure > &Obs);
    virtual FullPhysics::ArrayAdWithUnit< double,1 > pressure_grid() const;
    virtual int max_number_level() const;
    virtual boost::shared_ptr< FullPhysics::Pressure > clone() const;

/* Internal director utilities */
public:
    bool swig_get_inner(const char *swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }
    void swig_set_inner(const char *swig_protected_method_name, bool swig_val) const {
      swig_inner[swig_protected_method_name] = swig_val;
    }
private:
    mutable std::map<std::string, bool> swig_inner;

#if defined(SWIG_PYTHON_DIRECTOR_VTABLE)
/* VTable implementation */
    PyObject *swig_get_method(size_t method_index, const char *method_name) const {
      PyObject *method = vtable[method_index];
      if (!method) {
        swig::SwigVar_PyObject name = SWIG_Python_str_FromChar(method_name);
        method = PyObject_GetAttr(swig_get_self(), name);
        if (!method) {
          std::string msg = "Method in class Pressure doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[10];
#endif

};


#endif
