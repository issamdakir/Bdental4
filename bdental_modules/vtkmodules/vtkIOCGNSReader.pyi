from typing import overload, Any, Callable, TypeVar, Union
from typing import Tuple, List, Sequence, MutableSequence

Callback = Union[Callable[..., None], None]
Buffer = TypeVar('Buffer')
Pointer = TypeVar('Pointer')
Template = TypeVar('Template')

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonExecutionModel

class vtkCGNSFileSeriesReader(vtkmodules.vtkCommonExecutionModel.vtkMultiBlockDataSetAlgorithm):
    def AddFileName(self, fname:str) -> None: ...
    def CanReadFile(self, filename:str) -> int: ...
    def GetController(self) -> 'vtkMultiProcessController': ...
    def GetCurrentFileName(self) -> str: ...
    def GetIgnoreReaderTime(self) -> bool: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetReader(self) -> 'vtkCGNSReader': ...
    def IgnoreReaderTimeOff(self) -> None: ...
    def IgnoreReaderTimeOn(self) -> None: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkCGNSFileSeriesReader': ...
    def RemoveAllFileNames(self) -> None: ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkCGNSFileSeriesReader': ...
    def SetController(self, controller:'vtkMultiProcessController') -> None: ...
    def SetIgnoreReaderTime(self, _arg:bool) -> None: ...
    def SetReader(self, reader:'vtkCGNSReader') -> None: ...

class vtkCGNSReader(vtkmodules.vtkCommonExecutionModel.vtkMultiBlockDataSetAlgorithm):
    class DataArrayLocation(int): ...
    CELL_DATA:'DataArrayLocation'
    FACE_DATA:'DataArrayLocation'
    def Broadcast(self, ctrl:'vtkMultiProcessController') -> None: ...
    def CacheConnectivityOff(self) -> None: ...
    def CacheConnectivityOn(self) -> None: ...
    def CacheMeshOff(self) -> None: ...
    def CacheMeshOn(self) -> None: ...
    def CanReadFile(self, filename:str) -> int: ...
    def CreateEachSolutionAsBlockOff(self) -> None: ...
    def CreateEachSolutionAsBlockOn(self) -> None: ...
    def DisableAllBases(self) -> None: ...
    def DisableAllCellArrays(self) -> None: ...
    def DisableAllFaceArrays(self) -> None: ...
    def DisableAllFamilies(self) -> None: ...
    def DisableAllPointArrays(self) -> None: ...
    def DistributeBlocksOff(self) -> None: ...
    def DistributeBlocksOn(self) -> None: ...
    def DoublePrecisionMeshOff(self) -> None: ...
    def DoublePrecisionMeshOn(self) -> None: ...
    def EnableAllBases(self) -> None: ...
    def EnableAllCellArrays(self) -> None: ...
    def EnableAllFaceArrays(self) -> None: ...
    def EnableAllFamilies(self) -> None: ...
    def EnableAllPointArrays(self) -> None: ...
    @staticmethod
    def FAMILY() -> 'vtkInformationStringKey': ...
    def GetBaseArrayName(self, index:int) -> str: ...
    def GetBaseArrayStatus(self, name:str) -> int: ...
    def GetBaseSelection(self) -> 'vtkDataArraySelection': ...
    def GetCacheConnectivity(self) -> bool: ...
    def GetCacheMesh(self) -> bool: ...
    def GetCellArrayName(self, index:int) -> str: ...
    def GetCellArrayStatus(self, name:str) -> int: ...
    def GetController(self) -> 'vtkMultiProcessController': ...
    def GetCreateEachSolutionAsBlock(self) -> int: ...
    def GetDataLocation(self) -> int: ...
    def GetDataLocationMaxValue(self) -> int: ...
    def GetDataLocationMinValue(self) -> int: ...
    def GetDistributeBlocks(self) -> bool: ...
    def GetDoublePrecisionMesh(self) -> int: ...
    def GetFaceArrayName(self, index:int) -> str: ...
    def GetFaceArrayStatus(self, name:str) -> int: ...
    def GetFamilyArrayName(self, index:int) -> str: ...
    def GetFamilyArrayStatus(self, name:str) -> int: ...
    def GetFamilySelection(self) -> 'vtkDataArraySelection': ...
    def GetFileName(self) -> str: ...
    def GetIgnoreFlowSolutionPointers(self) -> bool: ...
    def GetLoadBndPatch(self) -> bool: ...
    def GetLoadMesh(self) -> bool: ...
    def GetNumberOfBaseArrays(self) -> int: ...
    def GetNumberOfCellArrays(self) -> int: ...
    def GetNumberOfFaceArrays(self) -> int: ...
    def GetNumberOfFamilyArrays(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetNumberOfPointArrays(self) -> int: ...
    def GetPointArrayName(self, index:int) -> str: ...
    def GetPointArrayStatus(self, name:str) -> int: ...
    def GetUnsteadySolutionStartTimestep(self) -> int: ...
    def GetUse3DVector(self) -> bool: ...
    def GetUseUnsteadyPattern(self) -> bool: ...
    def IgnoreFlowSolutionPointersOff(self) -> None: ...
    def IgnoreFlowSolutionPointersOn(self) -> None: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def LoadBndPatchOff(self) -> None: ...
    def LoadBndPatchOn(self) -> None: ...
    def LoadMeshOff(self) -> None: ...
    def LoadMeshOn(self) -> None: ...
    def NewInstance(self) -> 'vtkCGNSReader': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkCGNSReader': ...
    def SetBaseArrayStatus(self, name:str, status:int) -> None: ...
    def SetCacheConnectivity(self, enable:bool) -> None: ...
    def SetCacheMesh(self, enable:bool) -> None: ...
    def SetCellArrayStatus(self, name:str, status:int) -> None: ...
    def SetController(self, c:'vtkMultiProcessController') -> None: ...
    def SetCreateEachSolutionAsBlock(self, _arg:int) -> None: ...
    def SetDataLocation(self, _arg:int) -> None: ...
    def SetDistributeBlocks(self, _arg:bool) -> None: ...
    def SetDoublePrecisionMesh(self, _arg:int) -> None: ...
    def SetFaceArrayStatus(self, name:str, status:int) -> None: ...
    def SetFamilyArrayStatus(self, name:str, status:int) -> None: ...
    def SetFileName(self, arg:str) -> None: ...
    def SetIgnoreFlowSolutionPointers(self, _arg:bool) -> None: ...
    def SetLoadBndPatch(self, _arg:bool) -> None: ...
    def SetLoadMesh(self, _arg:bool) -> None: ...
    def SetPointArrayStatus(self, name:str, status:int) -> None: ...
    def SetUnsteadySolutionStartTimestep(self, _arg:int) -> None: ...
    def SetUse3DVector(self, _arg:bool) -> None: ...
    def SetUseUnsteadyPattern(self, _arg:bool) -> None: ...
    def Use3DVectorOff(self) -> None: ...
    def Use3DVectorOn(self) -> None: ...
    def UseUnsteadyPatternOff(self) -> None: ...
    def UseUnsteadyPatternOn(self) -> None: ...
