# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.9
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (3,0,0):
    new_instancemethod = lambda func, inst, cls: _aerosol_property.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_aerosol_property', [dirname(__file__)])
        except ImportError:
            import _aerosol_property
            return _aerosol_property
        if fp is not None:
            try:
                _mod = imp.load_module('_aerosol_property', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _aerosol_property = swig_import_helper()
    del swig_import_helper
else:
    import _aerosol_property
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x


class SwigPyIterator(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _aerosol_property.delete_SwigPyIterator
    def __iter__(self): return self
SwigPyIterator.value = new_instancemethod(_aerosol_property.SwigPyIterator_value,None,SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_aerosol_property.SwigPyIterator_incr,None,SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_aerosol_property.SwigPyIterator_decr,None,SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_aerosol_property.SwigPyIterator_distance,None,SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_aerosol_property.SwigPyIterator_equal,None,SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_aerosol_property.SwigPyIterator_copy,None,SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_aerosol_property.SwigPyIterator_next,None,SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_aerosol_property.SwigPyIterator___next__,None,SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_aerosol_property.SwigPyIterator_previous,None,SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_aerosol_property.SwigPyIterator_advance,None,SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_aerosol_property.SwigPyIterator___eq__,None,SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_aerosol_property.SwigPyIterator___ne__,None,SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_aerosol_property.SwigPyIterator___iadd__,None,SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_aerosol_property.SwigPyIterator___isub__,None,SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_aerosol_property.SwigPyIterator___add__,None,SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_aerosol_property.SwigPyIterator___sub__,None,SwigPyIterator)
SwigPyIterator_swigregister = _aerosol_property.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

SHARED_PTR_DISOWN = _aerosol_property.SHARED_PTR_DISOWN
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

import full_physics_swig.observer
import full_physics_swig.generic_object
import full_physics_swig.state_vector
class ObservableAerosolProperty(full_physics_swig.generic_object.GenericObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _aerosol_property.delete_ObservableAerosolProperty
ObservableAerosolProperty.add_observer_and_keep_reference = new_instancemethod(_aerosol_property.ObservableAerosolProperty_add_observer_and_keep_reference,None,ObservableAerosolProperty)
ObservableAerosolProperty.add_observer = new_instancemethod(_aerosol_property.ObservableAerosolProperty_add_observer,None,ObservableAerosolProperty)
ObservableAerosolProperty.remove_observer = new_instancemethod(_aerosol_property.ObservableAerosolProperty_remove_observer,None,ObservableAerosolProperty)
ObservableAerosolProperty_swigregister = _aerosol_property.ObservableAerosolProperty_swigregister
ObservableAerosolProperty_swigregister(ObservableAerosolProperty)

class ObserverAerosolProperty(full_physics_swig.generic_object.GenericObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self): 
        _aerosol_property.ObserverAerosolProperty_swiginit(self,_aerosol_property.new_ObserverAerosolProperty())
    __swig_destroy__ = _aerosol_property.delete_ObserverAerosolProperty
ObserverAerosolProperty.notify_update = new_instancemethod(_aerosol_property.ObserverAerosolProperty_notify_update,None,ObserverAerosolProperty)
ObserverAerosolProperty.notify_add = new_instancemethod(_aerosol_property.ObserverAerosolProperty_notify_add,None,ObserverAerosolProperty)
ObserverAerosolProperty.notify_remove = new_instancemethod(_aerosol_property.ObserverAerosolProperty_notify_remove,None,ObserverAerosolProperty)
ObserverAerosolProperty_swigregister = _aerosol_property.ObserverAerosolProperty_swigregister
ObserverAerosolProperty_swigregister(ObserverAerosolProperty)

class AerosolProperty(full_physics_swig.state_vector.StateVectorObserver,ObservableAerosolProperty):
    """
    This gives the Aerosol properties for an Aerosol.

    Our current AerosolProperty - AerosolPropertyHdf - doesn't make any
    use of our StateVector, we don't have aerosol properties in it. But we
    may want to have this in the future, so we've made this class a
    StateVectorObserver.

    Other objects may depend on the AerosolProperty, and should be updated
    when the AerosolProperty is updated. To facilitate that, this class in
    an Oberverable, and objects can add themselves as Observers to be
    notified when the AerosolProperty is updated.

    When implementing a new class, you almost always will want to derive
    from AerosolPropertyImpBase rather than from this class. See that
    class for a description.

    C++ includes: aerosol_property.h 
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _aerosol_property.delete_AerosolProperty
    def clone(self, *args):
        """
        virtual boost::shared_ptr<AerosolProperty> FullPhysics::AerosolProperty::clone(const boost::shared_ptr< Pressure > &Press) const =0
        This version of clone takes a pressure to use.

        The intent is that the pressure has been cloned from the original
        pressure (although this class has no way to verify this). This allows
        sets of objects to be cloned using a common Pressure clone, e.g.
        Atmosphere. 
        """
        return _aerosol_property.AerosolProperty_clone(self, *args)

    def extinction_coefficient_each_layer(self, *args):
        """
        virtual ArrayAd<double, 1> FullPhysics::AerosolProperty::extinction_coefficient_each_layer(double wn) const =0
        Return extinction coefficient for the given wave number, for each
        layer.

        Parameters:
        -----------

        wn:  - Wavenumber 
        """
        return _aerosol_property.AerosolProperty_extinction_coefficient_each_layer(self, *args)

    def scattering_coefficient_each_layer(self, *args):
        """
        virtual ArrayAd<double, 1> FullPhysics::AerosolProperty::scattering_coefficient_each_layer(double wn) const =0
        Return scattering coefficient for the given wave number for each
        layer.

        Parameters:
        -----------

        wn:  - Wavenumber 
        """
        return _aerosol_property.AerosolProperty_scattering_coefficient_each_layer(self, *args)

    def phase_function_moment_each_layer(self, *args):
        """
        virtual ArrayAd<double, 3> FullPhysics::AerosolProperty::phase_function_moment_each_layer(double wn, int nmom=-1, int nscatt=-1) const =0
        Return phase function moments for the given wave number for each
        layer.

        Note that we use the de Rooij convention for the scattering matrix
        moments.

        Parameters:
        -----------

        wn:  Wavenumber

        nmom:  Optional number of moments to return. Default is all moments.

        nscatt:  Optional number of scattering elements to return. Default is
        all of them.

        Phase function moment. This is nmom + 1 x nlayer x number scattering
        elements. 
        """
        return _aerosol_property.AerosolProperty_phase_function_moment_each_layer(self, *args)

AerosolProperty.clone = new_instancemethod(_aerosol_property.AerosolProperty_clone,None,AerosolProperty)
AerosolProperty.extinction_coefficient_each_layer = new_instancemethod(_aerosol_property.AerosolProperty_extinction_coefficient_each_layer,None,AerosolProperty)
AerosolProperty.scattering_coefficient_each_layer = new_instancemethod(_aerosol_property.AerosolProperty_scattering_coefficient_each_layer,None,AerosolProperty)
AerosolProperty.phase_function_moment_each_layer = new_instancemethod(_aerosol_property.AerosolProperty_phase_function_moment_each_layer,None,AerosolProperty)
AerosolProperty.__str__ = new_instancemethod(_aerosol_property.AerosolProperty___str__,None,AerosolProperty)
AerosolProperty_swigregister = _aerosol_property.AerosolProperty_swigregister
AerosolProperty_swigregister(AerosolProperty)

class vector_aerosol_property(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __iter__(self): return self.iterator()
    def __init__(self, *args): 
        _aerosol_property.vector_aerosol_property_swiginit(self,_aerosol_property.new_vector_aerosol_property(*args))
    __swig_destroy__ = _aerosol_property.delete_vector_aerosol_property
vector_aerosol_property.iterator = new_instancemethod(_aerosol_property.vector_aerosol_property_iterator,None,vector_aerosol_property)
vector_aerosol_property.__nonzero__ = new_instancemethod(_aerosol_property.vector_aerosol_property___nonzero__,None,vector_aerosol_property)
vector_aerosol_property.__bool__ = new_instancemethod(_aerosol_property.vector_aerosol_property___bool__,None,vector_aerosol_property)
vector_aerosol_property.__len__ = new_instancemethod(_aerosol_property.vector_aerosol_property___len__,None,vector_aerosol_property)
vector_aerosol_property.pop = new_instancemethod(_aerosol_property.vector_aerosol_property_pop,None,vector_aerosol_property)
vector_aerosol_property.__getslice__ = new_instancemethod(_aerosol_property.vector_aerosol_property___getslice__,None,vector_aerosol_property)
vector_aerosol_property.__setslice__ = new_instancemethod(_aerosol_property.vector_aerosol_property___setslice__,None,vector_aerosol_property)
vector_aerosol_property.__delslice__ = new_instancemethod(_aerosol_property.vector_aerosol_property___delslice__,None,vector_aerosol_property)
vector_aerosol_property.__delitem__ = new_instancemethod(_aerosol_property.vector_aerosol_property___delitem__,None,vector_aerosol_property)
vector_aerosol_property.__getitem__ = new_instancemethod(_aerosol_property.vector_aerosol_property___getitem__,None,vector_aerosol_property)
vector_aerosol_property.__setitem__ = new_instancemethod(_aerosol_property.vector_aerosol_property___setitem__,None,vector_aerosol_property)
vector_aerosol_property.append = new_instancemethod(_aerosol_property.vector_aerosol_property_append,None,vector_aerosol_property)
vector_aerosol_property.empty = new_instancemethod(_aerosol_property.vector_aerosol_property_empty,None,vector_aerosol_property)
vector_aerosol_property.size = new_instancemethod(_aerosol_property.vector_aerosol_property_size,None,vector_aerosol_property)
vector_aerosol_property.clear = new_instancemethod(_aerosol_property.vector_aerosol_property_clear,None,vector_aerosol_property)
vector_aerosol_property.swap = new_instancemethod(_aerosol_property.vector_aerosol_property_swap,None,vector_aerosol_property)
vector_aerosol_property.get_allocator = new_instancemethod(_aerosol_property.vector_aerosol_property_get_allocator,None,vector_aerosol_property)
vector_aerosol_property.begin = new_instancemethod(_aerosol_property.vector_aerosol_property_begin,None,vector_aerosol_property)
vector_aerosol_property.end = new_instancemethod(_aerosol_property.vector_aerosol_property_end,None,vector_aerosol_property)
vector_aerosol_property.rbegin = new_instancemethod(_aerosol_property.vector_aerosol_property_rbegin,None,vector_aerosol_property)
vector_aerosol_property.rend = new_instancemethod(_aerosol_property.vector_aerosol_property_rend,None,vector_aerosol_property)
vector_aerosol_property.pop_back = new_instancemethod(_aerosol_property.vector_aerosol_property_pop_back,None,vector_aerosol_property)
vector_aerosol_property.erase = new_instancemethod(_aerosol_property.vector_aerosol_property_erase,None,vector_aerosol_property)
vector_aerosol_property.push_back = new_instancemethod(_aerosol_property.vector_aerosol_property_push_back,None,vector_aerosol_property)
vector_aerosol_property.front = new_instancemethod(_aerosol_property.vector_aerosol_property_front,None,vector_aerosol_property)
vector_aerosol_property.back = new_instancemethod(_aerosol_property.vector_aerosol_property_back,None,vector_aerosol_property)
vector_aerosol_property.assign = new_instancemethod(_aerosol_property.vector_aerosol_property_assign,None,vector_aerosol_property)
vector_aerosol_property.resize = new_instancemethod(_aerosol_property.vector_aerosol_property_resize,None,vector_aerosol_property)
vector_aerosol_property.insert = new_instancemethod(_aerosol_property.vector_aerosol_property_insert,None,vector_aerosol_property)
vector_aerosol_property.reserve = new_instancemethod(_aerosol_property.vector_aerosol_property_reserve,None,vector_aerosol_property)
vector_aerosol_property.capacity = new_instancemethod(_aerosol_property.vector_aerosol_property_capacity,None,vector_aerosol_property)
vector_aerosol_property_swigregister = _aerosol_property.vector_aerosol_property_swigregister
vector_aerosol_property_swigregister(vector_aerosol_property)



