#coding=utf8

########################################################################
###                                                                  ###
### Created by Martin Genet, 2012-2018                               ###
###                                                                  ###
### University of California at San Francisco (UCSF), USA            ###
### Swiss Federal Institute of Technology (ETH), Zurich, Switzerland ###
### École Polytechnique, Palaiseau, France                           ###
###                                                                  ###
########################################################################

import vtk

import myPythonLibrary as mypy
import myVTKPythonLibrary as myvtk

########################################################################

def createUnsignedIntArray(
        name,
        n_components=1,
        n_tuples=0,
        init_to_zero=0,
        verbose=0):

    uiarray = vtk.vtkUnsignedIntArray()
    uiarray.SetName(name)
    uiarray.SetNumberOfComponents(n_components)
    uiarray.SetNumberOfTuples(n_tuples)

    if (init_to_zero):
        for k_tuple in xrange(n_tuples):
            uiarray.SetTuple(k_tuple, [0]*n_components)

    return uiarray
