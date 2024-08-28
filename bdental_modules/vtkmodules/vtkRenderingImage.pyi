from typing import overload, Any, Callable, TypeVar, Union
from typing import Tuple, List, Sequence, MutableSequence

Callback = Union[Callable[..., None], None]
Buffer = TypeVar('Buffer')
Pointer = TypeVar('Pointer')
Template = TypeVar('Template')

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkRenderingCore

class vtkDepthImageToPointCloud(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    def CullFarPointsOff(self) -> None: ...
    def CullFarPointsOn(self) -> None: ...
    def CullNearPointsOff(self) -> None: ...
    def CullNearPointsOn(self) -> None: ...
    def GetCamera(self) -> 'vtkCamera': ...
    def GetCullFarPoints(self) -> bool: ...
    def GetCullNearPoints(self) -> bool: ...
    def GetMTime(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetOutputPointsPrecision(self) -> int: ...
    def GetProduceColorScalars(self) -> bool: ...
    def GetProduceVertexCellArray(self) -> bool: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkDepthImageToPointCloud': ...
    def ProduceColorScalarsOff(self) -> None: ...
    def ProduceColorScalarsOn(self) -> None: ...
    def ProduceVertexCellArrayOff(self) -> None: ...
    def ProduceVertexCellArrayOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkDepthImageToPointCloud': ...
    def SetCamera(self, __a:'vtkCamera') -> None: ...
    def SetCullFarPoints(self, _arg:bool) -> None: ...
    def SetCullNearPoints(self, _arg:bool) -> None: ...
    def SetOutputPointsPrecision(self, _arg:int) -> None: ...
    def SetProduceColorScalars(self, _arg:bool) -> None: ...
    def SetProduceVertexCellArray(self, _arg:bool) -> None: ...

class vtkImageResliceMapper(vtkmodules.vtkRenderingCore.vtkImageMapper3D):
    def AutoAdjustImageQualityOff(self) -> None: ...
    def AutoAdjustImageQualityOn(self) -> None: ...
    def GetAutoAdjustImageQuality(self) -> int: ...
    @overload
    def GetBounds(self) -> Tuple[float, float, float, float, float, float]: ...
    @overload
    def GetBounds(self, bounds:MutableSequence[float]) -> None: ...
    def GetImageSampleFactor(self) -> int: ...
    def GetImageSampleFactorMaxValue(self) -> int: ...
    def GetImageSampleFactorMinValue(self) -> int: ...
    def GetIndexBounds(self, extent:MutableSequence[float]) -> None: ...
    def GetInterpolator(self) -> 'vtkAbstractImageInterpolator': ...
    def GetJumpToNearestSlice(self) -> int: ...
    def GetMTime(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetResampleToScreenPixels(self) -> int: ...
    def GetSeparateWindowLevelOperation(self) -> int: ...
    def GetSlabSampleFactor(self) -> int: ...
    def GetSlabSampleFactorMaxValue(self) -> int: ...
    def GetSlabSampleFactorMinValue(self) -> int: ...
    def GetSlabThickness(self) -> float: ...
    def GetSlabType(self) -> int: ...
    def GetSlabTypeAsString(self) -> str: ...
    def GetSlabTypeMaxValue(self) -> int: ...
    def GetSlabTypeMinValue(self) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def JumpToNearestSliceOff(self) -> None: ...
    def JumpToNearestSliceOn(self) -> None: ...
    def NewInstance(self) -> 'vtkImageResliceMapper': ...
    def ReleaseGraphicsResources(self, __a:'vtkWindow') -> None: ...
    def Render(self, renderer:'vtkRenderer', prop:'vtkImageSlice') -> None: ...
    def ResampleToScreenPixelsOff(self) -> None: ...
    def ResampleToScreenPixelsOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkImageResliceMapper': ...
    def SeparateWindowLevelOperationOff(self) -> None: ...
    def SeparateWindowLevelOperationOn(self) -> None: ...
    def SetAutoAdjustImageQuality(self, _arg:int) -> None: ...
    def SetImageSampleFactor(self, _arg:int) -> None: ...
    def SetInterpolator(self, interpolator:'vtkAbstractImageInterpolator') -> None: ...
    def SetJumpToNearestSlice(self, _arg:int) -> None: ...
    def SetResampleToScreenPixels(self, _arg:int) -> None: ...
    def SetSeparateWindowLevelOperation(self, _arg:int) -> None: ...
    def SetSlabSampleFactor(self, _arg:int) -> None: ...
    def SetSlabThickness(self, _arg:float) -> None: ...
    def SetSlabType(self, _arg:int) -> None: ...
    def SetSlabTypeToMax(self) -> None: ...
    def SetSlabTypeToMean(self) -> None: ...
    def SetSlabTypeToMin(self) -> None: ...
    def SetSlabTypeToSum(self) -> None: ...
    def SetSlicePlane(self, plane:'vtkPlane') -> None: ...

class vtkImageSliceCollection(vtkmodules.vtkRenderingCore.vtkPropCollection):
    def AddItem(self, a:'vtkImageSlice') -> None: ...
    def GetNextImage(self) -> 'vtkImageSlice': ...
    def GetNextItem(self) -> 'vtkImageSlice': ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkImageSliceCollection': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkImageSliceCollection': ...
    def Sort(self) -> None: ...

class vtkImageStack(vtkmodules.vtkRenderingCore.vtkImageSlice):
    def AddImage(self, prop:'vtkImageSlice') -> None: ...
    def BuildPaths(self, paths:'vtkAssemblyPaths', path:'vtkAssemblyPath') -> None: ...
    def GetActiveImage(self) -> 'vtkImageSlice': ...
    def GetActiveLayer(self) -> int: ...
    @overload
    def GetBounds(self) -> Tuple[float, float, float, float, float, float]: ...
    @overload
    def GetBounds(self, bounds:MutableSequence[float]) -> None: ...
    @overload
    def GetImages(self) -> 'vtkImageSliceCollection': ...
    @overload
    def GetImages(self, __a:'vtkPropCollection') -> None: ...
    def GetMTime(self) -> int: ...
    def GetMapper(self) -> 'vtkImageMapper3D': ...
    def GetNextPath(self) -> 'vtkAssemblyPath': ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetNumberOfPaths(self) -> int: ...
    def GetProperty(self) -> 'vtkImageProperty': ...
    def GetRedrawMTime(self) -> int: ...
    def HasImage(self, prop:'vtkImageSlice') -> int: ...
    def HasTranslucentPolygonalGeometry(self) -> int: ...
    def InitPathTraversal(self) -> None: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkImageStack': ...
    def ReleaseGraphicsResources(self, win:'vtkWindow') -> None: ...
    def RemoveImage(self, prop:'vtkImageSlice') -> None: ...
    def RenderOpaqueGeometry(self, viewport:'vtkViewport') -> int: ...
    def RenderOverlay(self, viewport:'vtkViewport') -> int: ...
    def RenderTranslucentPolygonalGeometry(self, viewport:'vtkViewport') -> int: ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkImageStack': ...
    def SetActiveLayer(self, _arg:int) -> None: ...
    def ShallowCopy(self, prop:'vtkProp') -> None: ...
