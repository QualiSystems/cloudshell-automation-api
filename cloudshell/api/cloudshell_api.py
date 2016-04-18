# encoding=utf8
__author__ = 'g8y3e'

import socket
import base64

from common_cloudshell_api import CommonAPISession
from common_cloudshell_api import CommonResponseInfo
from common_cloudshell_api import CommonAPIRequest

from collections import OrderedDict

class DeployAppInput(CommonAPIRequest):
    def __init__(self, AppName, Name, Value):
        """
            :param str AppName: constructor parameter
            :param str Name: constructor parameter
            :param str Value: constructor parameter
        """
        CommonAPIRequest.__init__(self, AppName=AppName, Name=Name, Value=Value)

class InputNameValue(CommonAPIRequest):
    def __init__(self, Name, Value):
        """
            :param str Name: constructor parameter
            :param str Value: constructor parameter
        """
        CommonAPIRequest.__init__(self, Name=Name, Value=Value)

class AttributeNameValue(CommonAPIRequest):
    def __init__(self, Name, Value):
        """
            :param str Name: constructor parameter
            :param str Value: constructor parameter
        """
        CommonAPIRequest.__init__(self, Name=Name, Value=Value)

class ResourceAttributesUpdateRequest(CommonAPIRequest):
    def __init__(self, ResourceFullName, AttributeNamesValues):
        """
            :param str ResourceFullName: constructor parameter
            :param list[AttributeNameValue] AttributeNamesValues: constructor parameter
        """
        CommonAPIRequest.__init__(self, ResourceFullName=ResourceFullName, AttributeNamesValues=AttributeNamesValues)

class UpdateTopologyGlobalInputsRequest(CommonAPIRequest):
    def __init__(self, ParamName, Value):
        """
            :param str ParamName: constructor parameter
            :param str Value: constructor parameter
        """
        CommonAPIRequest.__init__(self, ParamName=ParamName, Value=Value)

class UpdateTopologyRequirementsInputsRequest(CommonAPIRequest):
    def __init__(self, ResourceName, ParamName, Value, Type):
        """
            :param str ResourceName: constructor parameter
            :param str ParamName: constructor parameter
            :param str Value: constructor parameter
            :param str Type: constructor parameter
        """
        CommonAPIRequest.__init__(self, ResourceName=ResourceName, ParamName=ParamName, Value=Value, Type=Type)

class UpdateTopologyAdditionalInfoInputsRequest(CommonAPIRequest):
    def __init__(self, ResourceName, ParamName, Value):
        """
            :param str ResourceName: constructor parameter
            :param str ParamName: constructor parameter
            :param str Value: constructor parameter
        """
        CommonAPIRequest.__init__(self, ResourceName=ResourceName, ParamName=ParamName, Value=Value)

class UpdateRouteAliasRequest(CommonAPIRequest):
    def __init__(self, SourceResourceName, TargetResourceName, Alias):
        """
            :param str SourceResourceName: constructor parameter
            :param str TargetResourceName: constructor parameter
            :param str Alias: constructor parameter
        """
        CommonAPIRequest.__init__(self, SourceResourceName=SourceResourceName, TargetResourceName=TargetResourceName, Alias=Alias)

class ResourceInfoDto(CommonAPIRequest):
    def __init__(self, Family, Model, FullName, Address, FolderFullpath, ParentFullName, Description):
        """
            :param str Family: constructor parameter
            :param str Model: constructor parameter
            :param str FullName: constructor parameter
            :param str Address: constructor parameter
            :param str FolderFullpath: constructor parameter
            :param str ParentFullName: constructor parameter
            :param str Description: constructor parameter
        """
        CommonAPIRequest.__init__(self, Family=Family, Model=Model, FullName=FullName, Address=Address, FolderFullpath=FolderFullpath, ParentFullName=ParentFullName, Description=Description)

class PhysicalConnectionUpdateRequest(CommonAPIRequest):
    def __init__(self, ResourceAFullName, ResourceBFullName, ConnectionWeight):
        """
            :param str ResourceAFullName: constructor parameter
            :param str ResourceBFullName: constructor parameter
            :param str ConnectionWeight: constructor parameter
        """
        CommonAPIRequest.__init__(self, ResourceAFullName=ResourceAFullName, ResourceBFullName=ResourceBFullName, ConnectionWeight=ConnectionWeight)

class Attribute(CommonAPIRequest):
    def __init__(self, Name, RestrictedValue):
        """
            :param str Name: constructor parameter
            :param str RestrictedValue: constructor parameter
        """
        CommonAPIRequest.__init__(self, Name=Name, RestrictedValue=RestrictedValue)

class AddRestrictionRequest(CommonAPIRequest):
    def __init__(self, FamilyName, ModelName, Alphabetic, Attributes):
        """
            :param str FamilyName: constructor parameter
            :param str ModelName: constructor parameter
            :param str Alphabetic: constructor parameter
            :param list[Attribute] Attributes: constructor parameter
        """
        CommonAPIRequest.__init__(self, FamilyName=FamilyName, ModelName=ModelName, Alphabetic=Alphabetic, Attributes=Attributes)

class UserUpdateRequest(CommonAPIRequest):
    def __init__(self, Username, MaxConcurrentReservations, MaxReservationDuration):
        """
            :param str Username: constructor parameter
            :param str MaxConcurrentReservations: constructor parameter
            :param str MaxReservationDuration: constructor parameter
        """
        CommonAPIRequest.__init__(self, Username=Username, MaxConcurrentReservations=MaxConcurrentReservations, MaxReservationDuration=MaxReservationDuration)

class SetConnectorRequest(CommonAPIRequest):
    def __init__(self, SourceResourceFullName, TargetResourceFullName, Direction, Alias):
        """
            :param str SourceResourceFullName: constructor parameter
            :param str TargetResourceFullName: constructor parameter
            :param str Direction: constructor parameter
            :param str Alias: constructor parameter
        """
        CommonAPIRequest.__init__(self, SourceResourceFullName=SourceResourceFullName, TargetResourceFullName=TargetResourceFullName, Direction=Direction, Alias=Alias)

class RemoveRestrictionRequest(CommonAPIRequest):
    def __init__(self, FamilyName, ModelName, Attributes):
        """
            :param str FamilyName: constructor parameter
            :param str ModelName: constructor parameter
            :param list[Attribute] Attributes: constructor parameter
        """
        CommonAPIRequest.__init__(self, FamilyName=FamilyName, ModelName=ModelName, Attributes=Attributes)

class ResourceLockInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.ReservationName = str
        """:type : str"""
        self.MachineName = str
        """:type : str"""
        self.Username = str
        """:type : str"""
        self.Created = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class TopologyShortInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Alias = str
        """:type : str"""
        self.State = str
        """:type : str"""
        self.Type = str
        """:type : str"""
        self.Name = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class Group(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Role = str
        """:type : str"""
        self.Name = str
        """:type : str"""
        self.Description = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class Topology(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Name = str
        """:type : str"""
        self.Description = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class Resource(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Path = str
        """:type : str"""
        self.Name = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class DomainInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Archived  = str
        """:type : str"""
        self.TopologiesFolder = str
        """:type : str"""
        self.Name = str
        """:type : str"""
        self.Description = str
        """:type : str"""
        self.Topologies = {'list': Topology}
        """:type : list[Topology]"""
        self.Resources = {'list': Resource}
        """:type : list[Resource]"""
        self.Groups = {'list': Group}
        """:type : list[Group]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class VmCustomParam(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Name = str
        """:type : str"""
        self.Value = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class VmDetail(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.UID = str
        """:type : str"""
        self.CloudProviderFullName = str
        """:type : str"""
        self.VmCustomParams = {'list': VmCustomParam}
        """:type : list[VmCustomParam]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ResourceAttribute(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Type = str
        """:type : str"""
        self.Name = str
        """:type : str"""
        self.Value = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class Domain(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Name = str
        """:type : str"""
        self.Description = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class Connection(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.FullPath = str
        """:type : str"""
        self.Weight = int
        """:type : int"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ResourceInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.ResourceLiveStatusDescription = str
        """:type : str"""
        self.Locked = bool
        """:type : bool"""
        self.Name = str
        """:type : str"""
        self.UniqeIdentifier = str
        """:type : str"""
        self.Permission = str
        """:type : str"""
        self.FullAddress = str
        """:type : str"""
        self.ResourceLiveStatusName = str
        """:type : str"""
        self.ResourceFamilyName = str
        """:type : str"""
        self.RootAddress = str
        """:type : str"""
        self.DriverName = str
        """:type : str"""
        self.Excluded = bool
        """:type : bool"""
        self.Address = str
        """:type : str"""
        self.FolderFullPath = str
        """:type : str"""
        self.LockInfo = ResourceLockInfo
        """:type : ResourceLockInfo"""
        self.ResourceModelName = str
        """:type : str"""
        self.Description = str
        """:type : str"""
        self.Domains = {'list': Domain}
        """:type : list[Domain]"""
        self.Connections = {'list': Connection}
        """:type : list[Connection]"""
        self.ChildResources = {'list': object}
        """:type : list[ResourceInfo]"""
        self.ResourceAttributes = {'list': ResourceAttribute}
        """:type : list[ResourceAttribute]"""
        self.VmDetails = {'list': VmDetail}
        """:type : list[VmDetail]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ResourceLiveStatusInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.liveStatusName = str
        """:type : str"""
        self.liveStatusDescription = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ReservationLiveStatusInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.ReservationLiveStatuses = {'list': ReservationLiveStatus}
        """:type : list[ReservationLiveStatus]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ReservationLiveStatus(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.ReservationLiveStatusDescription = str
        """:type : str"""
        self.ReservationId = str
        """:type : str"""
        self.ReservationLiveStatusName = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class EndPointConnectionInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Routes = {'list': RouteInfo}
        """:type : list[RouteInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class VisualConnectorsInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Connectors = {'list': Connector}
        """:type : list[Connector]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class TopologyResourceInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Locked = bool
        """:type : bool"""
        self.Name = str
        """:type : str"""
        self.FullAddress = str
        """:type : str"""
        self.ResourceFamilyName = str
        """:type : str"""
        self.Alias = str
        """:type : str"""
        self.RootAddress = str
        """:type : str"""
        self.Excluded = bool
        """:type : bool"""
        self.Address = str
        """:type : str"""
        self.FolderFullPath = str
        """:type : str"""
        self.LockInfo = ResourceLockInfo
        """:type : ResourceLockInfo"""
        self.ResourceModelName = str
        """:type : str"""
        self.WillBeLocked = bool
        """:type : bool"""
        self.Connections = {'list': Connection}
        """:type : list[Connection]"""
        self.ResourceAttributes = {'list': ResourceAttribute}
        """:type : list[ResourceAttribute]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ActiveTopologyResourceInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Locked = bool
        """:type : bool"""
        self.Name = str
        """:type : str"""
        self.FullAddress = str
        """:type : str"""
        self.ResourceFamilyName = str
        """:type : str"""
        self.Alias = str
        """:type : str"""
        self.RootAddress = str
        """:type : str"""
        self.Address = str
        """:type : str"""
        self.FolderFullPath = str
        """:type : str"""
        self.LockInfo = ResourceLockInfo
        """:type : ResourceLockInfo"""
        self.ResourceModelName = str
        """:type : str"""
        self.Connections = {'list': Connection}
        """:type : list[Connection]"""
        self.ResourceAttributes = {'list': ResourceAttribute}
        """:type : list[ResourceAttribute]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class AbstractResourceAttribute(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Type = str
        """:type : str"""
        self.Name = str
        """:type : str"""
        self.Value = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class AbstractResourceRequiredAttribute(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Type = str
        """:type : str"""
        self.Name = str
        """:type : str"""
        self.Value = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class TopologyAbstractResourceInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.WillBeLocked = bool
        """:type : bool"""
        self.ResourceModelName = str
        """:type : str"""
        self.Alias = str
        """:type : str"""
        self.Valid = bool
        """:type : bool"""
        self.ResourceFamilyName = str
        """:type : str"""
        self.Quantity = int
        """:type : int"""
        self.Attributes = {'list': AbstractResourceAttribute}
        """:type : list[AbstractResourceAttribute]"""
        self.RequiredAttributes = {'list': AbstractResourceRequiredAttribute}
        """:type : list[AbstractResourceRequiredAttribute]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class RouteSegmentInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Source = str
        """:type : str"""
        self.Target = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class RouteInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Target = str
        """:type : str"""
        self.Source = str
        """:type : str"""
        self.RouteConfiguration = RouteConfigurationInfo
        """:type : RouteConfigurationInfo"""
        self.Alias = str
        """:type : str"""
        self.Shared = bool
        """:type : bool"""
        self.IsTap = bool
        """:type : bool"""
        self.RouteType = str
        """:type : str"""
        self.Attributes = {'list': RouteAttributeInfo}
        """:type : list[RouteAttributeInfo]"""
        self.Segments = {'list': RouteSegmentInfo}
        """:type : list[RouteSegmentInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ReservationAppResource(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.LogicalResource = LogicalResourceInfo
        """:type : LogicalResourceInfo"""
        self.Name = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class Connector(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Alias = str
        """:type : str"""
        self.Direction = str
        """:type : str"""
        self.Type = str
        """:type : str"""
        self.Target = str
        """:type : str"""
        self.Source = str
        """:type : str"""
        self.Attributes = {'list': AttributeValueInfo}
        """:type : list[AttributeValueInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class LogicalResourceInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Model = str
        """:type : str"""
        self.Family = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class RouteConfigurationInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Interface = long
        """:type : long"""
        self.Duplex = long
        """:type : long"""
        self.Speed = long
        """:type : long"""
        self.SpeedSetting = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class RouteAttributeInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.AttributeName = str
        """:type : str"""
        self.AttributeValue = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class CategoryListInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Categories = {'list': str}
        """:type : list[str]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class TopologiesByCategoryInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Topologies = {'list': str}
        """:type : list[str]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class CategoriesOfTopologyInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Categories = {'list': TopologyCategoryInfo}
        """:type : list[TopologyCategoryInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class TopologyCategoryInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Name = str
        """:type : str"""
        self.Value = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class TopologyInputsInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.DefaultValue = str
        """:type : str"""
        self.Description = str
        """:type : str"""
        self.ParamName = str
        """:type : str"""
        self.PossibleValues = {'list': str}
        """:type : list[str]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class TopologyGlobalInputsInfo(TopologyInputsInfo):
    def __init__(self, xml_object, find_prefix):
        TopologyInputsInfo.__init__(self, xml_object, find_prefix)

class TopologyAdditionalInfoInputsInfo(TopologyInputsInfo):
    def __init__(self, xml_object, find_prefix):
        self.ResourceName = str
        """:type : str"""
        self.LinkedToGlobal = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)
        TopologyInputsInfo.__init__(self, xml_object, find_prefix)

class TopologyRequirementsInputsInfo(TopologyInputsInfo):
    def __init__(self, xml_object, find_prefix):
        self.ResourceName = str
        """:type : str"""
        self.LinkedToGlobal = str
        """:type : str"""
        self.InputType = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)
        TopologyInputsInfo.__init__(self, xml_object, find_prefix)

class TopologyInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Name = str
        """:type : str"""
        self.Driver = str
        """:type : str"""
        self.Alias = str
        """:type : str"""
        self.State = str
        """:type : str"""
        self.Owner = str
        """:type : str"""
        self.ParentTopology = TopologyShortInfo
        """:type : TopologyShortInfo"""
        self.Type = str
        """:type : str"""
        self.Instructions = str
        """:type : str"""
        self.AbstractResources = {'list': TopologyAbstractResourceInfo}
        """:type : list[TopologyAbstractResourceInfo]"""
        self.Services = {'list': ServiceInstance}
        """:type : list[ServiceInstance]"""
        self.Connectors = {'list': Connector}
        """:type : list[Connector]"""
        self.AdditionalInfoInputs = {'list': TopologyAdditionalInfoInputsInfo}
        """:type : list[TopologyAdditionalInfoInputsInfo]"""
        self.Routes = {'list': RouteInfo}
        """:type : list[RouteInfo]"""
        self.GlobalInputs = {'list': TopologyGlobalInputsInfo}
        """:type : list[TopologyGlobalInputsInfo]"""
        self.RequirementsInputs = {'list': TopologyRequirementsInputsInfo}
        """:type : list[TopologyRequirementsInputsInfo]"""
        self.Resources = {'list': TopologyResourceInfo}
        """:type : list[TopologyResourceInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ActiveTopologyInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Username = str
        """:type : str"""
        self.MachineName = str
        """:type : str"""
        self.Name = str
        """:type : str"""
        self.Topology = str
        """:type : str"""
        self.Routes = {'list': RouteInfo}
        """:type : list[RouteInfo]"""
        self.Connectors = {'list': Connector}
        """:type : list[Connector]"""
        self.Resources = {'list': ActiveTopologyResourceInfo}
        """:type : list[ActiveTopologyResourceInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class TopologyListInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Topologies = {'list': str}
        """:type : list[str]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class AttributeValueInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Name = str
        """:type : str"""
        self.Value = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ResourceShortInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Locked = bool
        """:type : bool"""
        self.Name = str
        """:type : str"""
        self.Permission = str
        """:type : str"""
        self.FullAddress = str
        """:type : str"""
        self.ResourceFamilyName = str
        """:type : str"""
        self.RootAddress = str
        """:type : str"""
        self.Excluded = bool
        """:type : bool"""
        self.Address = str
        """:type : str"""
        self.FolderFullPath = str
        """:type : str"""
        self.LockInfo = ResourceLockInfo
        """:type : ResourceLockInfo"""
        self.ResourceModelName = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ResourceListInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Resources = {'list': ResourceShortInfo}
        """:type : list[ResourceShortInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ServiceInstance(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Alias = str
        """:type : str"""
        self.ServiceName = str
        """:type : str"""
        self.Attributes = {'list': AttributeValueInfo}
        """:type : list[AttributeValueInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ServiceAttribute(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Name = str
        """:type : str"""
        self.DefaultValue = str
        """:type : str"""
        self.IsRequired = bool
        """:type : bool"""
        self.RestrictedValues = str
        """:type : str"""
        self.PossibleValues = str
        """:type : str"""
        self.Type = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ServiceInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.CategoryFullPath = str
        """:type : str"""
        self.Name = str
        """:type : str"""
        self.Description = str
        """:type : str"""
        self.Attributes = {'list': ServiceAttribute}
        """:type : list[ServiceAttribute]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ServicesListInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Services = {'list': ServiceInfo}
        """:type : list[ServiceInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ContentShortInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Type = str
        """:type : str"""
        self.Name = str
        """:type : str"""
        self.Permission = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ContentListInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.ContentArray = {'list': ContentShortInfo}
        """:type : list[ContentShortInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ReservationListInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Reservations = {'list': ReservationInfo}
        """:type : list[ReservationInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ReservationInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Owner = str
        """:type : str"""
        self.Created = str
        """:type : str"""
        self.Id = str
        """:type : str"""
        self.Name = str
        """:type : str"""
        self.LockedResources = {'list': ResourceShortInfo}
        """:type : list[ResourceShortInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class Mapping(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Source = str
        """:type : str"""
        self.Target = str
        """:type : str"""
        self.RouteType = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ResourceMappingsInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Mapping = Mapping
        """:type : Mapping"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class CreateReservationResponseInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Reservation = ReservationShortInfo
        """:type : ReservationShortInfo"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ReplaceWithResourceResponseInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.RootResources = {'list': str}
        """:type : list[str]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class GetReservationsInRangeResponseInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Reservations = {'list': ReservationShortInfo}
        """:type : list[ReservationShortInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ReservationShortInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Status = str
        """:type : str"""
        self.ReservationLiveStatusDescription = str
        """:type : str"""
        self.Booked = bool
        """:type : bool"""
        self.ProvisioningStatus = str
        """:type : str"""
        self.Description = str
        """:type : str"""
        self.ReservationLiveStatusName = str
        """:type : str"""
        self.DomainName = str
        """:type : str"""
        self.CreateDate = str
        """:type : str"""
        self.ModificationDate = str
        """:type : str"""
        self.ActualEndTime = str
        """:type : str"""
        self.RecurrenceType = str
        """:type : str"""
        self.StartTime = str
        """:type : str"""
        self.Owner = str
        """:type : str"""
        self.EndTime = str
        """:type : str"""
        self.Id = str
        """:type : str"""
        self.Name = str
        """:type : str"""
        self.Topologies = {'list': str}
        """:type : list[str]"""
        self.PermittedUsers = {'list': str}
        """:type : list[str]"""
        self.TopologiesInfo = {'list': TopologyShortInfo}
        """:type : list[TopologyShortInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ReservationDiagramLayoutResponseInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.ResourceDiagramLayouts = {'list': ResourceDiagramLayoutInfo}
        """:type : list[ResourceDiagramLayoutInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ResourceDiagramLayoutInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Y = float
        """:type : float"""
        self.ResourceName = str
        """:type : str"""
        self.X = float
        """:type : float"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class GetReservationDescriptionResponseInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.ReservationDescription = ReservationDescriptionInfo
        """:type : ReservationDescriptionInfo"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ReservationDescriptionInfo(ReservationShortInfo):
    def __init__(self, xml_object, find_prefix):
        self.ReservationLiveStatus = ReservationLiveStatus
        """:type : ReservationLiveStatus"""
        self.TopologiesInstructionsInfo = {'list': TopologyInstructionsInfo}
        """:type : list[TopologyInstructionsInfo]"""
        self.TopologiesResourcesAttributeInfo = {'list': TopologiesResourcesAttributesInfo}
        """:type : list[TopologiesResourcesAttributesInfo]"""
        self.Apps = {'list': ReservationAppResource}
        """:type : list[ReservationAppResource]"""
        self.ActiveRoutesInfo = {'list': RouteInfo}
        """:type : list[RouteInfo]"""
        self.TopologiesReservedResources = {'list': TopologyReservedResourceInfo}
        """:type : list[TopologyReservedResourceInfo]"""
        self.Connectors = {'list': Connector}
        """:type : list[Connector]"""
        self.Services = {'list': ServiceInstance}
        """:type : list[ServiceInstance]"""
        self.Conflicts = {'list': ResourceConflictInfo}
        """:type : list[ResourceConflictInfo]"""
        self.RequestedRoutesInfo = {'list': RouteInfo}
        """:type : list[RouteInfo]"""
        self.Resources = {'list': ReservedResourceInfo}
        """:type : list[ReservedResourceInfo]"""
        self.TopologiesRouteInfo = {'list': TopologyRoutesInfo}
        """:type : list[TopologyRoutesInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)
        ReservationShortInfo.__init__(self, xml_object, find_prefix)

class GetReservationInputsResponseInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.GlobalInputs = {'list': ReservedTopologyGlobalInputsInfo}
        """:type : list[ReservedTopologyGlobalInputsInfo]"""
        self.AdditionalInfoInputs = {'list': ReservedTopologyAdditionalInfoInputsInfo}
        """:type : list[ReservedTopologyAdditionalInfoInputsInfo]"""
        self.RequiredInputs = {'list': ReservedTopologyRequiredInputsInfo}
        """:type : list[ReservedTopologyRequiredInputsInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ReservedTopologyInputsInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Value = str
        """:type : str"""
        self.ParamName = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ReservedTopologyGlobalInputsInfo(ReservedTopologyInputsInfo):
    def __init__(self, xml_object, find_prefix):
        self.PossibleValues = {'list': str}
        """:type : list[str]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)
        ReservedTopologyInputsInfo.__init__(self, xml_object, find_prefix)

class ReservedTopologyRequiredInputsInfo(ReservedTopologyInputsInfo):
    def __init__(self, xml_object, find_prefix):
        self.ResourceName = str
        """:type : str"""
        self.LinkedToGlobal = str
        """:type : str"""
        self.Type = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)
        ReservedTopologyInputsInfo.__init__(self, xml_object, find_prefix)

class ReservedTopologyAdditionalInfoInputsInfo(ReservedTopologyInputsInfo):
    def __init__(self, xml_object, find_prefix):
        self.ResourceName = str
        """:type : str"""
        self.LinkedToGlobal = str
        """:type : str"""
        self.PossibleValues = {'list': str}
        """:type : list[str]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)
        ReservedTopologyInputsInfo.__init__(self, xml_object, find_prefix)

class TopologiesResourcesAttributesInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Usage = str
        """:type : str"""
        self.Alias = str
        """:type : str"""
        self.AttributeName = str
        """:type : str"""
        self.Name = str
        """:type : str"""
        self.TopologyName = str
        """:type : str"""
        self.AttributeValue = {'list': str}
        """:type : list[str]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ReservedResourceInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Locked = bool
        """:type : bool"""
        self.Name = str
        """:type : str"""
        self.FullAddress = str
        """:type : str"""
        self.ResourceFamilyName = str
        """:type : str"""
        self.Released = bool
        """:type : bool"""
        self.FolderFullPath = str
        """:type : str"""
        self.Shared = bool
        """:type : bool"""
        self.ResourceModelName = str
        """:type : str"""
        self.Availability = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class TopologyRoutesInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.TopologyName = str
        """:type : str"""
        self.Routes = {'list': RouteInfo}
        """:type : list[RouteInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class TopologyInstructionsInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.TopologyName = str
        """:type : str"""
        self.Instructions = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class TopologyReservedResourceInfo(ReservedResourceInfo):
    def __init__(self, xml_object, find_prefix):
        self.Alias = str
        """:type : str"""
        self.TopologyName = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)
        ReservedResourceInfo.__init__(self, xml_object, find_prefix)

class GetActiveReservationsResponseInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Reservations = {'list': ReservationShortInfo}
        """:type : list[ReservationShortInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ResourceConflictInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.ConflictWith = str
        """:type : str"""
        self.ConflictType = str
        """:type : str"""
        self.ConflictStarted = str
        """:type : str"""
        self.ResourceName = str
        """:type : str"""
        self.ConflictWithUser = str
        """:type : str"""
        self.ConflictPlannedEndTime = str
        """:type : str"""
        self.Topology = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ReserveResourcesResponseInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Conflicts = {'list': ResourceConflictInfo}
        """:type : list[ResourceConflictInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class AddAppToReservationResponseInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.ReservedAppName = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ReserveTopologyResponseInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Conflicts = {'list': ResourceConflictInfo}
        """:type : list[ResourceConflictInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class CommandExecutionIdResponseInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Id = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class CommandExecutionResultInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        pass

class CommandExecutionResultListInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Results = {'list': CommandExecutionResultInfo}
        """:type : list[CommandExecutionResultInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class CommandExecutionCompletedResultInfo(CommandExecutionResultInfo):
    def __init__(self, xml_object, find_prefix):
        self.Output = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)
        CommandExecutionResultInfo.__init__(self, xml_object, find_prefix)

class CommandExecutionCancelledResultInfo(CommandExecutionResultInfo):
    def __init__(self, xml_object, find_prefix):
        self.Message = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)
        CommandExecutionResultInfo.__init__(self, xml_object, find_prefix)

class CommandExecutionFailedResultInfo(CommandExecutionResultInfo):
    def __init__(self, xml_object, find_prefix):
        self.ErrorDescription = str
        """:type : str"""
        self.ErrorName = str
        """:type : str"""
        self.ErrorParameters = {'list': ErrorParameter}
        """:type : list[ErrorParameter]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)
        CommandExecutionResultInfo.__init__(self, xml_object, find_prefix)

class ErrorParameter(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Name = str
        """:type : str"""
        self.Value = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class LogonDomainInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.DomainId = str
        """:type : str"""
        self.Name = str
        """:type : str"""
        self.Description = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class LogonTokenInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Token = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class LogonResponseInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Domain = LogonDomainInfo
        """:type : LogonDomainInfo"""
        self.Token = LogonTokenInfo
        """:type : LogonTokenInfo"""
        self.User = UserInfo
        """:type : UserInfo"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class CommandParameter(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Mandatory = bool
        """:type : bool"""
        self.Name = str
        """:type : str"""
        self.DefaultValue = str
        """:type : str"""
        self.EnumValues = str
        """:type : str"""
        self.Type = str
        """:type : str"""
        self.Description = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ResourceCommandInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Tag = str
        """:type : str"""
        self.DisplayName = str
        """:type : str"""
        self.Name = str
        """:type : str"""
        self.Description = str
        """:type : str"""
        self.Parameters = {'list': CommandParameter}
        """:type : list[CommandParameter]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ResourceCommandListInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Commands = {'list': ResourceCommandInfo}
        """:type : list[ResourceCommandInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class TopologyCommandInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Name = str
        """:type : str"""
        self.Description = str
        """:type : str"""
        self.Parameters = {'list': CommandParameter}
        """:type : list[CommandParameter]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class TopologyCommandListInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Commands = {'list': TopologyCommandInfo}
        """:type : list[TopologyCommandInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class EnvironmentCommandListInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Commands = {'list': EnvironmentCommandInfo}
        """:type : list[EnvironmentCommandInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class EnvironmentCommandParameter(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Mandatory = bool
        """:type : bool"""
        self.Name = str
        """:type : str"""
        self.DefaultValue = str
        """:type : str"""
        self.EnumValues = str
        """:type : str"""
        self.DisplayName = str
        """:type : str"""
        self.Type = str
        """:type : str"""
        self.Description = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class EnvironmentCommandInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.DisplayName = str
        """:type : str"""
        self.Name = str
        """:type : str"""
        self.Description = str
        """:type : str"""
        self.Parameters = {'list': EnvironmentCommandParameter}
        """:type : list[EnvironmentCommandParameter]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class FindResourceReservationInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.ResourceFullName = str
        """:type : str"""
        self.ReservationName = str
        """:type : str"""
        self.ReservationId = str
        """:type : str"""
        self.StartTime = str
        """:type : str"""
        self.Owner = str
        """:type : str"""
        self.Shared = bool
        """:type : bool"""
        self.EndTime = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ResourcesUsageSummaryInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.NumOfNotInReservation = int
        """:type : int"""
        self.NumOfShared = int
        """:type : int"""
        self.NumOfReserved = int
        """:type : int"""
        self.ResourceFullName = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class FindResourceInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.ReservedStatus = str
        """:type : str"""
        self.Description = str
        """:type : str"""
        self.UsageSummary = ResourcesUsageSummaryInfo
        """:type : ResourcesUsageSummaryInfo"""
        self.FullAddress = str
        """:type : str"""
        self.Permission = str
        """:type : str"""
        self.ConnectedTo = str
        """:type : str"""
        self.ResourceFamilyName = str
        """:type : str"""
        self.Excluded = bool
        """:type : bool"""
        self.Address = str
        """:type : str"""
        self.FullName = str
        """:type : str"""
        self.ResourceModelName = str
        """:type : str"""
        self.FullPath = str
        """:type : str"""
        self.Name = str
        """:type : str"""
        self.Reservations = {'list': FindResourceReservationInfo}
        """:type : list[FindResourceReservationInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class FindResourceListInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Resources = {'list': FindResourceInfo}
        """:type : list[FindResourceInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class GetReservationRemainingTimeInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.RemainingTimeInMinutes = float
        """:type : float"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class UsersInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Users = {'list': UserInfo}
        """:type : list[UserInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class UserInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.IsDomainAdmin = bool
        """:type : bool"""
        self.Name = str
        """:type : str"""
        self.DomainName = str
        """:type : str"""
        self.IsAdmin = bool
        """:type : bool"""
        self.Email = str
        """:type : str"""
        self.IsActive = bool
        """:type : bool"""
        self.Groups = {'list': GroupInfo}
        """:type : list[GroupInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class GroupsInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Groups = {'list': GroupInfo}
        """:type : list[GroupInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class TestShellDomainInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Id = str
        """:type : str"""
        self.Name = str
        """:type : str"""
        self.Description = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class GroupInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.GroupRole = str
        """:type : str"""
        self.Name = str
        """:type : str"""
        self.Description = str
        """:type : str"""
        self.TestShellDomains = {'list': TestShellDomainInfo}
        """:type : list[TestShellDomainInfo]"""
        self.Users = {'list': UserInfo}
        """:type : list[UserInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class UtilizationReport(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.UtilizationReportRows = {'list': UtilizationReportRow}
        """:type : list[UtilizationReportRow]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class UtilizationReportRow(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Model = str
        """:type : str"""
        self.ParentId = str
        """:type : str"""
        self.Name = str
        """:type : str"""
        self.Family = str
        """:type : str"""
        self.Utilization = float
        """:type : float"""
        self.Children = {'list': object}
        """:type : list[UtilizationReportRow]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ServerTimeInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.ServerDateTime = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class ExportConfigurationInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Configuration = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class GetServerTimeZonesResponse(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.TimeZones = {'list': TimeZoneDefinition}
        """:type : list[TimeZoneDefinition]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class TimeZoneDefinition(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.DisplayName = str
        """:type : str"""
        self.Id = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class AbstractTemplateShortInfoList(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.AbstractTemplates = {'list': AbstractTemplateShortInfo}
        """:type : list[AbstractTemplateShortInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class AbstractTemplateShortInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Description = str
        """:type : str"""
        self.DomainName = str
        """:type : str"""
        self.CreateDate = str
        """:type : str"""
        self.ResourceModelName = str
        """:type : str"""
        self.Valid = bool
        """:type : bool"""
        self.Owner = str
        """:type : str"""
        self.ResourceFamilyName = str
        """:type : str"""
        self.Name = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class BulkAppDeploymentyResultItem(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.ErrorCode = int
        """:type : int"""
        self.AppDeploymentyInfo = AppDeploymentyInfo
        """:type : AppDeploymentyInfo"""
        self.AppName = str
        """:type : str"""
        self.Success = bool
        """:type : bool"""
        self.Error = str
        """:type : str"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class BulkAppDeploymentyInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.ResultItems = {'list': BulkAppDeploymentyResultItem}
        """:type : list[BulkAppDeploymentyResultItem]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class AppDeploymentyInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.VmUuid = str
        """:type : str"""
        self.CloudProviderResourceName = str
        """:type : str"""
        self.LogicalResourceName = str
        """:type : str"""
        self.VisualConnectors = {'list': AppVisualConnector}
        """:type : list[AppVisualConnector]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class AppVisualConnector(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Alias = str
        """:type : str"""
        self.Target = str
        """:type : str"""
        self.Source = str
        """:type : str"""
        self.Attributes = {'list': AttributeValueInfo}
        """:type : list[AttributeValueInfo]"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class NumericRange(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.Start = int
        """:type : int"""
        self.End = int
        """:type : int"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class VlanPoolRangeNumericInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.VlanRange = NumericRange
        """:type : NumericRange"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class VlanPoolSingleNumericInfo(CommonResponseInfo):
    def __init__(self, xml_object, find_prefix):
        self.VlanId = int
        """:type : int"""
        CommonResponseInfo.__init__(self, xml_object, find_prefix)

class CloudShellAPISession(CommonAPISession):
    def __init__(self, host, username='', password='', domain='', timezone='UTC', datetimeformat='MM/dd/yyyy HH:mm',
                 token_id='', port=8029, uri='/ResourceManagerApiService/'):
        CommonAPISession.__init__(self, host, username, password, domain)

        self.port = str(port)
        self.hostname = socket.gethostname() + ':' + self.port
        self.url = 'http://' + host + ':' + self.port + uri
        self.headers = {
            'Content-Type': 'text/xml',
            'Accept': '*/*',
            'ClientTimeZoneId': timezone,
            'DateTimeFormat': datetimeformat
        }

        self._encodeHeaders()

        self.token_id = token_id
        response_info = None
        if len(token_id) == 0:
            response_info = self.Logon(username, password, domain)
        else:
            response_info = self.SecureLogon(token_id, domain)

        self.domain = response_info.Domain.DomainId
        self.token_id = response_info.Token.Token

    def _sendRequest(self, username, domain, operation, message):
        request_headers = self.headers.copy()

        request_headers['Content-Length'] = len(message)
        request_headers['Host'] = self.host + ':' + self.port

        request_headers['Authorization'] = 'MachineName=' + self.hostname + \
                                           ';Token=' + self.token_id

        return CommonAPISession._sendRequest(self, operation, message, request_headers)


    def UpdateDriver(self, driverName='', driverFileName=''):
        """
            Updating driver in cloudshell

            :param driverName: str
            :param driverFile: str
            :param driverFileName: str
            :return: string
        """
        driverFile = open(driverFileName,'rb').read()

        return self.generateAPIRequest(OrderedDict([('method_name', 'UpdateDriver'), ('driverName', driverName), ('driverFile', base64.b64encode(driverFile)),
                                                    ('driverFileName', driverFileName)]))

    def UpdateScript(self, scriptName='', scriptFileName=''):
        """
            Updating driver in cloudshell

            :param driverName: str
            :param driverFile: str
            :param driverFileName: str
            :return: string
        """
        scriptFile = open(scriptFileName, 'rb').read()

        return self.generateAPIRequest(OrderedDict([('method_name', 'UpdateScript'), ('scriptName', scriptName), ('scriptFile', base64.b64encode(scriptFile)),
                                                    ('scriptFileName', scriptFileName)]))

    def ActivateTopology(self, reservationId='', topologyFullPath=''):
        """
            Activates a specified topology.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str topologyFullPath: Specify the full topology name. Include the full path from the root to the topology, separated by slashes. For example: FolderName/Topologies/TopologyName.

            :rtype: ActiveTopologyInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'ActivateTopology'), ('reservationId', reservationId), ('topologyFullPath', topologyFullPath)]))

    def AddGroupsToDomain(self, domainName='', groupNames=[], readOnly=False):
        """
            Add groups to a domain.

            :param str domainName: Specify the name of the domain.
            :param list[str] groupNames: Specify an array of one or more groups.
            :param bool readOnly: Specify if the array of group should be added with view only permissions.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'AddGroupsToDomain'), ('domainName', domainName), ('groupNames', groupNames), ('readOnly', readOnly)]))

    def AddNewDomain(self, domainName='', description=''):
        """
            Adds a new domain.

            :param str domainName: Specify the name of the domain.
            :param str description: Specify the description of the domain.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'AddNewDomain'), ('domainName', domainName), ('description', description)]))

    def AddNewGroup(self, groupName='', description='', groupRole=''):
        """
            Adds a new users group

            :param str groupName: Specify the name of the group.
            :param str description: Provide a short description of the group.
            :param str groupRole: Specify the role of the group, possible values: External, Regular, DomainAdmin.

            :rtype: GroupInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'AddNewGroup'), ('groupName', groupName), ('description', description), ('groupRole', groupRole)]))

    def AddNewUser(self, username='', password='', email='', isActive=False, isAdmin=False):
        """
            Configures user login details and permissions. Use AddUsersToGroup to specify the user’s domain access.

            :param str username: Specify the name of the user.
            :param str password: Specify the user’s login password.
            :param str email: Specify the user’s email address.
            :param bool isActive: Grant or deny active access to the application.
            :param bool isAdmin: Add the user to the System Administrators group.

            :rtype: UserInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'AddNewUser'), ('username', username), ('password', password), ('email', email), ('isActive', isActive), ('isAdmin', isAdmin)]))

    def AddPermittedUsersToReservation(self, reservationId='', usernames=[]):
        """
            Add one or more permitted users to the specified reservation.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param list[str] usernames: List of users to permit access to the reservation.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'AddPermittedUsersToReservation'), ('reservationId', reservationId), ('usernames', usernames)]))

    def AddResourcesToDomain(self, domainName='', resourcesNames=[], includeDecendants=True):
        """
            Add resources to a domain.

            :param str domainName: Specify the name of the domain.
            :param list[str] resourcesNames: Specify a list of resource names. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/ResourceName
            :param bool includeDecendants: Specify whether to include child resources.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'AddResourcesToDomain'), ('domainName', domainName), ('resourcesNames', resourcesNames), ('includeDecendants', includeDecendants)]))

    def AddResourcesToReservation(self, reservationId='', resourcesFullPath=[], shared=False):
        """
            Reserves resources to be locked.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param list[str] resourcesFullPath: Specify a list of resource names. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/ResourceName
            :param bool shared: Specify whether all resources will be shared among other enviroments

            :rtype: ReserveResourcesResponseInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'AddResourcesToReservation'), ('reservationId', reservationId), ('resourcesFullPath', resourcesFullPath), ('shared', shared)]))

    def AddRoutesToReservation(self, reservationId='', sourceResourcesFullPath=[], targetResourcesFullPath=[], mappingType='', maxHops=0, routeAlias='', isShared=False):
        """
            Adds (but does not connect) routes between all pairs of source and target endpoints, adding additional connectivity ports when required. Use ConnectRoutesInReservation to connect the routes.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param list[str] sourceResourcesFullPath: Specify a list of resource names. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/ResourceName
            :param list[str] targetResourcesFullPath: Specify a list of resource names. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/ResourceName
            :param str mappingType: Specify bidirectional or unidirectional as the mapping type.
            :param int maxHops: Specify the maximum number or allowed hops.
            :param str routeAlias: Specify the route’s alias.
            :param bool isShared: Specify whether these routes are shared. Shared routes can be used in more than one reservation.

            :rtype: RouteInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'AddRoutesToReservation'), ('reservationId', reservationId), ('sourceResourcesFullPath', sourceResourcesFullPath), ('targetResourcesFullPath', targetResourcesFullPath), ('mappingType', mappingType), ('maxHops', maxHops), ('routeAlias', routeAlias), ('isShared', isShared)]))

    def AddTopologiesToDomain(self, domainName='', topologyNames=[]):
        """
            Adds a list of one or more topologies to a domain.

            :param str domainName: Specify the name of the domain.
            :param list[str] topologyNames: Specify a list of topology names. Include the full path from the root to the topology, separated by slashes. For example: FolderName/Topologies/TopologyName.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'AddTopologiesToDomain'), ('domainName', domainName), ('topologyNames', topologyNames)]))

    def AddTopologyToReservation(self, reservationId='', topologyFullPath='', globalInputs=[], requirementsInputs=[], additionalInfoInputs=[]):
        """
            Reserves the specified topology.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str topologyFullPath: Specify the full topology name. Include the full path from the root to the topology, separated by slashes. For example: FolderName/Topologies/TopologyName.
            :param list[UpdateTopologyGlobalInputsRequest] globalInputs: Global inputs associated with the specified topology. For example: {['Input Name', 'Value';]}.
            :param list[UpdateTopologyRequirementsInputsRequest] requirementsInputs: Requirements inputs associated with the specified topology. For example: {['Resource Name', 'Input Name', 'Value', 'AttributeType';]}, AttributeType can be one of the following: Attributes/Models/Quantity. 
            :param list[UpdateTopologyAdditionalInfoInputsRequest] additionalInfoInputs: Additional info inputs associated with the specified topology. For example: {['Resource Name', 'Input Name', 'Value';]}. 

            :rtype: ReserveTopologyResponseInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'AddTopologyToReservation'), ('reservationId', reservationId), ('topologyFullPath', topologyFullPath), ('globalInputs', CommonAPIRequest.toContainer(globalInputs)), ('requirementsInputs', CommonAPIRequest.toContainer(requirementsInputs)), ('additionalInfoInputs', CommonAPIRequest.toContainer(additionalInfoInputs))]))

    def AddUsersToGroup(self, usernames=[], groupName=''):
        """
            Adds a list of one or more users to the specified group.

            :param list[str] usernames: Specify an array of one or more users.
            :param str groupName: Specify the name of the group.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'AddUsersToGroup'), ('usernames', usernames), ('groupName', groupName)]))

    def AutoLoad(self, resourceFullPath=''):
        """
            Overrides the data of a specified L1 switch with current device settings and mappings.

            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'AutoLoad'), ('resourceFullPath', resourceFullPath)]))

    def AddAttributeRestrictedValues(self, addAttributeRestrictionRequests=[]):
        """
            add attribute restrictions to family/model

            :param list[AddRestrictionRequest] addAttributeRestrictionRequests: Attribute restrictions to add. For example: {['FamilyName', 'ModelName', 'Alphabetic';]}.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'AddAttributeRestrictedValues'), ('addAttributeRestrictionRequests', CommonAPIRequest.toContainer(addAttributeRestrictionRequests))]))

    def ArchiveDomain(self, domainName=''):
        """
            Archive a domain. All future reservation will be deleted.

            :param str domainName: Specify the name of the domain.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'ArchiveDomain'), ('domainName', domainName)]))

    def AddAppToReservation(self, reservationId='', appName='', positionX=100, positionY=100):
        """
            Add app resource to existing reservation.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str appName: Specify the app template name.
            :param float positionX: Specify the x coordinate of the app's top left corner.
            :param float positionY: Specify the y coordinate of the app's top left corner.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'AddAppToReservation'), ('reservationId', reservationId), ('appName', appName), ('positionX', positionX), ('positionY', positionY)]))

    def AddServiceToReservation(self, reservationId='', serviceName='', alias='', attributes=[]):
        """
            Add service resource to existing reservation.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str serviceName: Specify the service name.
            :param str alias: Specify the service alias.
            :param list[AttributeNameValue] attributes: Specify a matrix of attributes and associated attribute values.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'AddServiceToReservation'), ('reservationId', reservationId), ('serviceName', serviceName), ('alias', alias), ('attributes', CommonAPIRequest.toContainer(attributes))]))

    def CopyDomainsResources(self, domainNameSources=[], domainNameDestination=''):
        """
            Copy resources from a list of source domains to a target domain.

            :param list[str] domainNameSources: Specify the names of the source domains.
            :param str domainNameDestination: Specify the name of the target domain.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'CopyDomainsResources'), ('domainNameSources', domainNameSources), ('domainNameDestination', domainNameDestination)]))

    def ClearAndResetConsole(self, reservationId='', resourceFullPath='', consolePortsFullPath=[], baudRate=0):
        """
            Clears and resets specified resource console ports.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.
            :param list[str] consolePortsFullPath: Specify a list of console ports according to their location in the Resource Explorer. Include the full path from the root to each console port, separated by slashes. For example: Console/Ports/PortName.
            :param int baudRate: Specify the baud rate to apply to the ports.

            :rtype: CommandExecutionCompletedResultInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'ClearAndResetConsole'), ('reservationId', reservationId), ('resourceFullPath', resourceFullPath), ('consolePortsFullPath', consolePortsFullPath), ('baudRate', baudRate)]))

    def ConnectRoutesInReservation(self, reservationId='', endpoints=[], mappingType=''):
        """
            Connects requested routes. It locks the resources and adds route mappings. The routes must already exist in the reservation.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param list[str] endpoints: The routes’ endpoints to connect.
            :param str mappingType: Specify bidirectional or unidirectional as the mapping type.

            :rtype: EndPointConnectionInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'ConnectRoutesInReservation'), ('reservationId', reservationId), ('endpoints', CommonAPIRequest.toContainer(endpoints)), ('mappingType', mappingType)]))

    def CreateFolder(self, folderFullPath=''):
        """
            Adds a new folder to the specified path.

            :param str folderFullPath: Specify the full folder name. Include the full path from the root to a specific folder, separated by slashes. For example: ResourceFamilyFolder/ResourceModelFolder.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'CreateFolder'), ('folderFullPath', folderFullPath)]))

    def CreateImmediateReservation(self, reservationName='', owner='', durationInMinutes=0, notifyOnStart=False, notifyOnEnd=False, notificationMinutesBeforeEnd=0):
        """
            Defines a reservation to be started immediately.

            :param str reservationName: Specify the name of the reservation.
            :param str owner: Specify the user name of the reservation owner.
            :param int durationInMinutes: Specify the length of the reservation. (in minutes)
            :param bool notifyOnStart: Indicate whether to notify the reservation owner when the reservation starts.
            :param bool notifyOnEnd: Indicate whether to notify the reservation owner when the reservation ends.
            :param int notificationMinutesBeforeEnd: Indicate the number of minutes before the end of the reservation to send out a Notify On End alert to the reservation owner. (0 = disabled)

            :rtype: CreateReservationResponseInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'CreateImmediateReservation'), ('reservationName', reservationName), ('owner', owner), ('durationInMinutes', durationInMinutes), ('notifyOnStart', notifyOnStart), ('notifyOnEnd', notifyOnEnd), ('notificationMinutesBeforeEnd', notificationMinutesBeforeEnd)]))

    def CreateImmediateTopologyReservation(self, reservationName='', owner='', durationInMinutes=0, notifyOnStart=False, notifyOnEnd=False, notificationMinutesBeforeEnd=0, topologyFullPath='', globalInputs=[], requirementsInputs=[], additionalInfoInputs=[]):
        """
            Defines a reservation to be started immediately.

            :param str reservationName: Specify the name of the reservation.
            :param str owner: Specify the user name of the reservation owner.
            :param int durationInMinutes: Specify the length of the reservation. (in minutes)
            :param bool notifyOnStart: Indicate whether to notify the reservation owner when the reservation starts.
            :param bool notifyOnEnd: Indicate whether to notify the reservation owner when the reservation ends.
            :param int notificationMinutesBeforeEnd: Indicate the number of minutes before the end of the reservation to send out a Notify On End alert to the reservation owner. (0 = disabled)
            :param str topologyFullPath: Specify the full topology name. Include the full path from the root to the topology, separated by slashes. For example: FolderName/Topologies/TopologyName.
            :param list[UpdateTopologyGlobalInputsRequest] globalInputs: Global inputs associated with the specified topology. For example: {['Input Name', 'Value';]}.
            :param list[UpdateTopologyRequirementsInputsRequest] requirementsInputs: Requirements inputs associated with the specified topology. For example: {['Resource Name', 'Input Name', 'Value', 'AttributeType';]}, AttributeType can be one of the following: Attributes/Models/Quantity. 
            :param list[UpdateTopologyAdditionalInfoInputsRequest] additionalInfoInputs: Additional info inputs associated with the specified topology. For example: {['Resource Name', 'Input Name', 'Value';]}. 

            :rtype: CreateReservationResponseInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'CreateImmediateReservation'), ('reservationName', reservationName), ('owner', owner), ('durationInMinutes', durationInMinutes), ('notifyOnStart', notifyOnStart), ('notifyOnEnd', notifyOnEnd), ('notificationMinutesBeforeEnd', notificationMinutesBeforeEnd), ('topologyFullPath', topologyFullPath), ('globalInputs', CommonAPIRequest.toContainer(globalInputs)), ('requirementsInputs', CommonAPIRequest.toContainer(requirementsInputs)), ('additionalInfoInputs', CommonAPIRequest.toContainer(additionalInfoInputs))]))

    def CreateReservation(self, reservationName='', owner='', startTime='', endTime='', notifyOnStart=False, notifyOnEnd=False, notificationMinutesBeforeEnd=0):
        """
            Defines a new reservation.

            :param str reservationName: Specify the name of the reservation.
            :param str owner: Specify the user name of the reservation owner.
            :param str startTime: The start time of the reservation.
            :param str endTime: The end time of the reservation.
            :param bool notifyOnStart: Indicate whether to notify the reservation owner when the reservation starts.
            :param bool notifyOnEnd: Indicate whether to notify the reservation owner when the reservation ends.
            :param int notificationMinutesBeforeEnd: Indicate the number of minutes before the end of the reservation to send out a Notify On End alert to the reservation owner. (0 = disabled)

            :rtype: CreateReservationResponseInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'CreateReservation'), ('reservationName', reservationName), ('owner', owner), ('startTime', startTime), ('endTime', endTime), ('notifyOnStart', notifyOnStart), ('notifyOnEnd', notifyOnEnd), ('notificationMinutesBeforeEnd', notificationMinutesBeforeEnd)]))

    def CreateTopologyReservation(self, reservationName='', owner='', startTime='', endTime='', notifyOnStart=False, notifyOnEnd=False, notificationMinutesBeforeEnd=0, topologyFullPath='', globalInputs=[], requirementsInputs=[], additionalInfoInputs=[]):
        """
            Defines a new reservation.

            :param str reservationName: Specify the name of the reservation.
            :param str owner: Specify the user name of the reservation owner.
            :param str startTime: The start time of the reservation.
            :param str endTime: The end time of the reservation.
            :param bool notifyOnStart: Indicate whether to notify the reservation owner when the reservation starts.
            :param bool notifyOnEnd: Indicate whether to notify the reservation owner when the reservation ends.
            :param int notificationMinutesBeforeEnd: Indicate the number of minutes before the end of the reservation to send out a Notify On End alert to the reservation owner. (0 = disabled)
            :param str topologyFullPath: Specify the full topology name. Include the full path from the root to the topology, separated by slashes. For example: FolderName/Topologies/TopologyName.
            :param list[UpdateTopologyGlobalInputsRequest] globalInputs: Global inputs associated with the specified topology. For example: {['Input Name', 'Value';]}.
            :param list[UpdateTopologyRequirementsInputsRequest] requirementsInputs: Requirements inputs associated with the specified topology. For example: {['Resource Name', 'Input Name', 'Value', 'AttributeType';]}, AttributeType can be one of the following: Attributes/Models/Quantity. 
            :param list[UpdateTopologyAdditionalInfoInputsRequest] additionalInfoInputs: Additional info inputs associated with the specified topology. For example: {['Resource Name', 'Input Name', 'Value';]}. 

            :rtype: CreateReservationResponseInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'CreateReservation'), ('reservationName', reservationName), ('owner', owner), ('startTime', startTime), ('endTime', endTime), ('notifyOnStart', notifyOnStart), ('notifyOnEnd', notifyOnEnd), ('notificationMinutesBeforeEnd', notificationMinutesBeforeEnd), ('topologyFullPath', topologyFullPath), ('globalInputs', CommonAPIRequest.toContainer(globalInputs)), ('requirementsInputs', CommonAPIRequest.toContainer(requirementsInputs)), ('additionalInfoInputs', CommonAPIRequest.toContainer(additionalInfoInputs))]))

    def CreateResource(self, resourceFamily='', resourceModel='', resourceName='', resourceAddress='', folderFullPath='', parentResourceFullPath='', resourceDescription=''):
        """
            Adds a new resource.

            :param str resourceFamily: Specify the name of the resource family.
            :param str resourceModel: Specify the resource model.
            :param str resourceName: Specify the resource name.
            :param str resourceAddress: Specify the resource address.
            :param str folderFullPath: Specify the full folder name. Include the full path from the root to a specific folder, separated by slashes. For example: ResourceFamilyFolder/ResourceModelFolder.
            :param str parentResourceFullPath: Specify the full path from the root to a parent resource, separated by slashes. For example: Traffic Generators/Generic.
            :param str resourceDescription: Provide a short description to help identify the resource.

            :rtype: ResourceInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'CreateResource'), ('resourceFamily', resourceFamily), ('resourceModel', resourceModel), ('resourceName', resourceName), ('resourceAddress', resourceAddress), ('folderFullPath', folderFullPath), ('parentResourceFullPath', parentResourceFullPath), ('resourceDescription', resourceDescription)]))

    def CreateResources(self, resourceInfoDtos=[]):
        """
            Adds new resources.

            :param list[ResourceInfoDto] resourceInfoDtos: Specify a matrix of resources to add. For example: {['Resource Family','Resource Model','Resource Name','Resource Address','Folder Full Path','Parent Resource Full Path','Resource Description';]}

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'CreateResources'), ('resourceInfoDtos', CommonAPIRequest.toContainer(resourceInfoDtos))]))

    def CreateRouteInReservation(self, reservationId='', sourceResourceFullPath='', targetResourceFullPath='', overrideActiveRoutes=False, mappingType='', maxHops=0, routeAlias='', isShared=False):
        """
            Creates a route between the specified source and target resources.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str sourceResourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.
            :param str targetResourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.
            :param bool overrideActiveRoutes: Specify whether the new route can override existing routes.
            :param str mappingType: Specify bidirectional or unidirectional as the mapping type.
            :param int maxHops: Specify the maximum number or allowed hops.
            :param str routeAlias: Specify the route’s alias.
            :param bool isShared: Specify whether this route is shared. Shared routes can be used in more than one reservation.

            :rtype: EndPointConnectionInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'CreateRouteInReservation'), ('reservationId', reservationId), ('sourceResourceFullPath', sourceResourceFullPath), ('targetResourceFullPath', targetResourceFullPath), ('overrideActiveRoutes', overrideActiveRoutes), ('mappingType', mappingType), ('maxHops', maxHops), ('routeAlias', routeAlias), ('isShared', isShared)]))

    def CreateRoutesInReservation(self, reservationId='', sourceResourcesFullPath=[], targetResourcesFullPath=[], overrideActiveRoutes=False, mappingType='', maxHops=0, routeAlias='', isShared=False):
        """
            Create routes between the listed source and target resources. Routes will be created for each pair of source and target resources.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param list[str] sourceResourcesFullPath: Specify a list of resource names. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/ResourceName
            :param list[str] targetResourcesFullPath: Specify a list of resource names. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/ResourceName
            :param bool overrideActiveRoutes: Specify whether the new route can override existing routes.
            :param str mappingType: Specify bidirectional or unidirectional as the mapping type.
            :param int maxHops: Specify the maximum number or allowed hops.
            :param str routeAlias: Specify the route’s alias.
            :param bool isShared: Specify whether these routes are shared. Shared routes can be used in more than one reservation.

            :rtype: EndPointConnectionInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'CreateRoutesInReservation'), ('reservationId', reservationId), ('sourceResourcesFullPath', sourceResourcesFullPath), ('targetResourcesFullPath', targetResourcesFullPath), ('overrideActiveRoutes', overrideActiveRoutes), ('mappingType', mappingType), ('maxHops', maxHops), ('routeAlias', routeAlias), ('isShared', isShared)]))

    def DeleteDomain(self, domainName=''):
        """
            Deletes a domain.

            :param str domainName: Specify the name of the domain.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'DeleteDomain'), ('domainName', domainName)]))

    def DeleteTopology(self, topologyFullPath=''):
        """
            Deletes the specified topology.

            :param str topologyFullPath: Specify the topology name. Include the full path from the root to the topology, separated by slashes. For example: FolderName/Topologies/TopologyName.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'DeleteTopology'), ('topologyFullPath', topologyFullPath)]))

    def DeleteFolder(self, folderFullPath=''):
        """
            Deletes the specified folder.

            :param str folderFullPath: Specify the full folder name. Include the full path from the root to a specific folder, separated by slashes. For example: ResourceFamilyFolder/ResourceModelFolder.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'DeleteFolder'), ('folderFullPath', folderFullPath)]))

    def DeleteGroup(self, groupName=''):
        """
            Deletes the specified group.

            :param str groupName: Specify the name of the group.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'DeleteGroup'), ('groupName', groupName)]))

    def DeleteReservation(self, reservationId='', unmap=False):
        """
            Deletes the specified reservation and optionally, releases all reservation resources.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param bool unmap: Specify whether to keep mappings or release mapped resources when deleting the reservation.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'DeleteReservation'), ('reservationId', reservationId), ('unmap', unmap)]))

    def DeleteResource(self, resourceFullPath=''):
        """
            Deletes the specified resource.

            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'DeleteResource'), ('resourceFullPath', resourceFullPath)]))

    def DeleteResources(self, resourcesFullPath=[]):
        """
            Deletes the specified resources.

            :param list[str] resourcesFullPath: Specify a list of resource names. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/ResourceName

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'DeleteResources'), ('resourcesFullPath', resourcesFullPath)]))

    def DeleteUser(self, username=''):
        """
            Deletes the specified user.

            :param str username: Specify the name of the user.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'DeleteUser'), ('username', username)]))

    def DisconnectRoutesInReservation(self, reservationId='', endpoints=[]):
        """
            Disconnects requested routes. It unlocks the resources (if locked), and removes route mappings, but does not remove the route resources from the reservation.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param list[str] endpoints: The routes endpoints to disconnect.

            :rtype: EndPointConnectionInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'DisconnectRoutesInReservation'), ('reservationId', reservationId), ('endpoints', CommonAPIRequest.toContainer(endpoints))]))

    def DecryptPassword(self, encryptedString=''):
        """
            Decrypt a password.

            :param str encryptedString: The encrypted string for decryption.

            :rtype: AttributeValueInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'DecryptPassword'), ('encryptedString', encryptedString)]))

    def DeleteResourceTemplate(self, resourceTemplateName=''):
        """
            Deletes a specific resource template.

            :param str resourceTemplateName: Specify the resource template name.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'DeleteResourceTemplate'), ('resourceTemplateName', resourceTemplateName)]))

    def EndReservation(self, reservationId='', unmap=False):
        """
            Ends the specified reservation and optionally, unlocks and releases all reservation resources.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param bool unmap: Specify whether to keep mappings or release mapped resources when deleting the reservation.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'EndReservation'), ('reservationId', reservationId), ('unmap', unmap)]))

    def ExcludeResource(self, resourceFullPath=''):
        """
            Excludes a specified resource.

            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'ExcludeResource'), ('resourceFullPath', resourceFullPath)]))

    def ExcludeResources(self, resourcesFullPath=[]):
        """
            Excludes the specified resources.

            :param list[str] resourcesFullPath: Specify a list of resource names. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/ResourceName

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'ExcludeResources'), ('resourcesFullPath', resourcesFullPath)]))

    def EnqueueResourceCommand(self, reservationId='', resourceFullPath='', commandName='', parameterValues=[], printOutput=False):
        """
            [Deprecated] Enqueues a command to be executed for the specified driver.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.
            :param str commandName: Specify the name of the command.
            :param list[str] parameterValues: Specify the list of parameters values required for executing the command.
            :param bool printOutput: Defines whether to print the command output in the reservation command output window.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'EnqueueResourceCommand'), ('reservationId', reservationId), ('resourceFullPath', resourceFullPath), ('commandName', commandName), ('parameterValues', parameterValues), ('printOutput', printOutput)]))

    def EnqueueServiceCommand(self, reservationId='', serviceAlias='', commandName='', parameterValues=[], printOutput=False):
        """
            [Deprecated] Enqueues a command to be executed for the specified driver.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str serviceAlias: Specify the alias of the service. The service alias is its identifier in the environment context. It can be retrieved via the environment details API and is displayed visually on the diagram.
            :param str commandName: Specify the name of the command.
            :param list[str] parameterValues: Specify the list of parameters values required for executing the command.
            :param bool printOutput: Defines whether to print the command output in the reservation command output window.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'EnqueueServiceCommand'), ('reservationId', reservationId), ('serviceAlias', serviceAlias), ('commandName', commandName), ('parameterValues', parameterValues), ('printOutput', printOutput)]))

    def ExecuteResourceCommand(self, reservationId='', resourceFullPath='', commandName='', parameterValues=[], printOutput=False):
        """
            [Deprecated] Executes a command for the specified driver.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.
            :param str commandName: Specify the name of the command.
            :param list[str] parameterValues: Specify the list of parameters values required for executing the command.
            :param bool printOutput: Defines whether to print the command output in the reservation command output window.

            :rtype: CommandExecutionCompletedResultInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'ExecuteResourceCommand'), ('reservationId', reservationId), ('resourceFullPath', resourceFullPath), ('commandName', commandName), ('parameterValues', parameterValues), ('printOutput', printOutput)]))

    def ExecuteResourceConnectedCommand(self, reservationId='', resourceFullPath='', commandName='', commandTag='', parameterValues=[], connectedPortsFullPath=[], printOutput=False):
        """
            Executes a command for the specified driver.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: RouterA/Port1.
            :param str commandName: Specify the name of the command.
            :param str commandTag: Specify the command tag. Connected command tags are used to define categories of functionality (e.g 'virtualization').
            :param list[str] parameterValues: Specify the list of parameters values required for executing the command.
            :param list[str] connectedPortsFullPath: Specify the list of connected ports to use in this operation. Include the full path from the root resource to each port, separated by slashes. For example: Switch20/Blade5/PowerPort1. Leave blank to perform the connected operation on all of the specified resource’s connected ports.
            :param bool printOutput: Defines whether to print the command output in the reservation command output window.

            :rtype: CommandExecutionCompletedResultInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'ExecuteResourceConnectedCommand'), ('reservationId', reservationId), ('resourceFullPath', resourceFullPath), ('commandName', commandName), ('commandTag', commandTag), ('parameterValues', parameterValues), ('connectedPortsFullPath', connectedPortsFullPath), ('printOutput', printOutput)]))

    def EnqueueTopologyCommand(self, reservationId='', commandName='', parameterValues=[], printOutput=False):
        """
            [Deprecated] Enqueues a command to be executed for the specified reservation.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str commandName: Specify the name of the command.
            :param list[str] parameterValues: Specify the list of parameters values required for executing the command.
            :param bool printOutput: Defines whether to print the command output in the reservation command output window.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'EnqueueTopologyCommand'), ('reservationId', reservationId), ('commandName', commandName), ('parameterValues', parameterValues), ('printOutput', printOutput)]))

    def ExecuteTopologyCommand(self, reservationId='', commandName='', parameterValues=[], printOutput=False):
        """
            [Deprecated] Executes a command for the specified reservation.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str commandName: Specify the name of the command.
            :param list[str] parameterValues: Specify the list of parameters values required for executing the command.
            :param bool printOutput: Defines whether to print the command output in the reservation command output window.

            :rtype: CommandExecutionCompletedResultInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'ExecuteTopologyCommand'), ('reservationId', reservationId), ('commandName', commandName), ('parameterValues', parameterValues), ('printOutput', printOutput)]))

    def ExtendReservation(self, reservationId='', minutesToAdd=0):
        """
            Extends the duration of the specified reservation.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param int minutesToAdd: Specify the number of minutes to add to the specified reservation.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'ExtendReservation'), ('reservationId', reservationId), ('minutesToAdd', minutesToAdd)]))

    def ExportFamiliesAndModels(self):
        """
            Exports the resource families, models, attributes and structure configuration.


            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'ExportFamiliesAndModels')]))

    def ExecuteServiceCommand(self, reservationId='', serviceAlias='', commandName='', parameterValues=[], printOutput=False):
        """
            [Deprecated] Executes a command for the specified service driver.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str serviceAlias: Specify the alias of the service.
            :param str commandName: Specify the name of the command.
            :param list[str] parameterValues: Specify the list of parameters values required for executing the command.
            :param bool printOutput: Defines whether to print the command output in the reservation command output window.

            :rtype: CommandExecutionCompletedResultInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'ExecuteServiceCommand'), ('reservationId', reservationId), ('serviceAlias', serviceAlias), ('commandName', commandName), ('parameterValues', parameterValues), ('printOutput', printOutput)]))

    def ExecuteDeployAppCommand(self, reservationId='', appName='', commandInputs=[], printOutput=False):
        """
            Executes deploy command for the specified app driver.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str appName: Specify the name of the app.
            :param list[InputNameValue] commandInputs: Specify a matrix of input names and values required for executing the command.
            :param bool printOutput: Defines whether to print the command output in the reservation command output window.

            :rtype: AppDeploymentyInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'ExecuteDeployAppCommand'), ('reservationId', reservationId), ('appName', appName), ('commandInputs', CommonAPIRequest.toContainer(commandInputs)), ('printOutput', printOutput)]))

    def ExecuteDeployAppCommandBulk(self, reservationId='', appNames=[], commandInputs=[], printOutput=False):
        """
            Executes deploy command for the specified apps.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param list[str] appNames: Specify the names of the apps to deploy.
            :param list[DeployAppInput] commandInputs: Specify a matrix of input names and values required for executing the command [appName, InputName, InputValue].
            :param bool printOutput: Defines whether to print the command output in the reservation command output window.

            :rtype: BulkAppDeploymentyInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'ExecuteDeployAppCommandBulk'), ('reservationId', reservationId), ('appNames', appNames), ('commandInputs', CommonAPIRequest.toContainer(commandInputs)), ('printOutput', printOutput)]))

    def ExecuteInstallAppCommand(self, reservationId='', resourceName='', commandName='', commandInputs=[], printOutput=False):
        """
            Executes install command for the specified app driver or script.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str resourceName: Specify the name of the resource deployment command created.
            :param str commandName: Specify the name of the command.
            :param list[InputNameValue] commandInputs: Specify a matrix of input names and values required for executing the command.
            :param bool printOutput: Defines whether to print the command output in the reservation command output window.

            :rtype: CommandExecutionCompletedResultInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'ExecuteInstallAppCommand'), ('reservationId', reservationId), ('resourceName', resourceName), ('commandName', commandName), ('commandInputs', CommonAPIRequest.toContainer(commandInputs)), ('printOutput', printOutput)]))

    def EnqueueEnvironmentCommand(self, reservationId='', commandName='', commandInputs=[], printOutput=False):
        """
            Enqueues a command to be executed for the specified reservation.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str commandName: Specify the name of the command.
            :param list[InputNameValue] commandInputs: Specify a matrix of input names and values required for executing the command.
            :param bool printOutput: Defines whether to print the command output in the reservation command output window.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'EnqueueEnvironmentCommand'), ('reservationId', reservationId), ('commandName', commandName), ('commandInputs', CommonAPIRequest.toContainer(commandInputs)), ('printOutput', printOutput)]))

    def ExecuteEnvironmentCommand(self, reservationId='', commandName='', commandInputs=[], printOutput=False):
        """
            Executes a command for the specified reservation.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str commandName: Specify the name of the command.
            :param list[InputNameValue] commandInputs: Specify a matrix of input names and values required for executing the command.
            :param bool printOutput: Defines whether to print the command output in the reservation command output window.

            :rtype: CommandExecutionCompletedResultInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'ExecuteEnvironmentCommand'), ('reservationId', reservationId), ('commandName', commandName), ('commandInputs', CommonAPIRequest.toContainer(commandInputs)), ('printOutput', printOutput)]))

    def EnqueueCommand(self, reservationId='', targetName='', targetType='', commandName='', commandInputs=[], printOutput=False):
        """
            Enqueues a command to be executed for the specified target.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str targetName: Specify the name of the target according to the target type: for resources - specify the resouce's name, for services - the service's alias.
            :param str targetType: Specify the target type for command execution.
            :param str commandName: Specify the name of the command.
            :param list[InputNameValue] commandInputs: Specify a matrix of input names and values required for executing the command.
            :param bool printOutput: Defines whether to print the command output in the reservation command output window.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'EnqueueCommand'), ('reservationId', reservationId), ('targetName', targetName), ('targetType', targetType), ('commandName', commandName), ('commandInputs', CommonAPIRequest.toContainer(commandInputs)), ('printOutput', printOutput)]))

    def ExecuteCommand(self, reservationId='', targetName='', targetType='', commandName='', commandInputs=[], printOutput=False):
        """
            Executes a command for the specified target.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str targetName: Specify the name of the target according to the target type: for resources - specify the resouce's name, for services - the service's alias.
            :param str targetType: Specify the target type for command execution.
            :param str commandName: Specify the name of the command.
            :param list[InputNameValue] commandInputs: Specify a matrix of input names and values required for executing the command.
            :param bool printOutput: Defines whether to print the command output in the reservation command output window.

            :rtype: CommandExecutionCompletedResultInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'ExecuteCommand'), ('reservationId', reservationId), ('targetName', targetName), ('targetType', targetType), ('commandName', commandName), ('commandInputs', CommonAPIRequest.toContainer(commandInputs)), ('printOutput', printOutput)]))

    def FindResources(self, resourceFamily='', resourceModel='', attributeValues=[], showAllDomains=False, resourceFullName='', exactName=True, includeSubResources=True, resourceAddress='', resourceUniqueIdentifier='', maxResults=500):
        """
            Retrieves resources that match all the specified search parameters, and all reservations associated with the search results.

            :param str resourceFamily: Specify the name of the resource family.
            :param str resourceModel: Specify the resource model.
            :param list[AttributeNameValue] attributeValues: Specify an array of one or more attributes and attribute values.
            :param bool showAllDomains: Show all domains associated with the logged in user.
            :param str resourceFullName: Specify part of or the full name of the resource.
            :param bool exactName: Specify whether to search the exact given name or not.
            :param bool includeSubResources: Specify whether to retrieve the sub resources once the parent matches the name.
            :param str resourceAddress: Specify the resource address. Can be partial (e.g. '192.168.').
            :param str resourceUniqueIdentifier: Specify the resource unique identifier.
            :param int maxResults: Specify the maximum number of resources to return.

            :rtype: FindResourceListInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'FindResources'), ('resourceFamily', resourceFamily), ('resourceModel', resourceModel), ('attributeValues', CommonAPIRequest.toContainer(attributeValues)), ('showAllDomains', showAllDomains), ('resourceFullName', resourceFullName), ('exactName', exactName), ('includeSubResources', includeSubResources), ('resourceAddress', resourceAddress), ('resourceUniqueIdentifier', resourceUniqueIdentifier), ('maxResults', maxResults)]))

    def FindResourcesInTimeRange(self, resourceFamily='', resourceModel='', fromTime='', untilTime='', attributeValues=[], showAllDomains=False, resourceFullName='', exactName=True, includeSubResources=True, resourceAddress='', resourceUniqueIdentifier='', maxResults=500):
        """
            Retrieves resources that match all the specified search parameters, and all reservations in the specified time range associated with the search results.

            :param str resourceFamily: Specify the name of the resource family.
            :param str resourceModel: Specify the resource model.
            :param str fromTime: Specify from which time and date to check the resource's availability.
            :param str untilTime: Specify until which time and date to check the resource's availability.
            :param list[AttributeNameValue] attributeValues: Specify an array of one or more attributes and attribute values.
            :param bool showAllDomains: Show all domains associated with the logged in user.
            :param str resourceFullName: Specify part of or the full name of the resource.
            :param bool exactName: Specify whether to search the exact given name or not.
            :param bool includeSubResources: Specify whether to retrieve the sub resources once the parent matches the name.
            :param str resourceAddress: Specify the resource address. Can be partial (e.g. '192.168.').
            :param str resourceUniqueIdentifier: Specify the resource unique identifier.
            :param int maxResults: Specify the maximum number of resources to return.

            :rtype: FindResourceListInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'FindResourcesInTimeRange'), ('resourceFamily', resourceFamily), ('resourceModel', resourceModel), ('fromTime', fromTime), ('untilTime', untilTime), ('attributeValues', CommonAPIRequest.toContainer(attributeValues)), ('showAllDomains', showAllDomains), ('resourceFullName', resourceFullName), ('exactName', exactName), ('includeSubResources', includeSubResources), ('resourceAddress', resourceAddress), ('resourceUniqueIdentifier', resourceUniqueIdentifier), ('maxResults', maxResults)]))

    def GetReservationResourcesPositions(self, reservationId=''):
        """
            Retrieves the x/y coordinates for all resources in the reservation's diagram.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.

            :rtype: ReservationDiagramLayoutResponseInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetReservationResourcesPositions'), ('reservationId', reservationId)]))

    def GetRoutesSolution(self, reservationId='', sourceResourcesFullPath=[], targetResourcesFullPath=[], mappingType='', maxHops=0, isShared=False):
        """
            Calculates possible routes between the supplied endpoints and returns their details, without saving, connecting or modifying the reservation in any way.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param list[str] sourceResourcesFullPath: Specify a list of resource names. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: RootResourceName/ResourceName
            :param list[str] targetResourcesFullPath: Specify a list of resource names. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: RootResourceName/ResourceName
            :param str mappingType: Specify bidirectional or unidirectional as the mapping type.
            :param int maxHops: Specify the maximum number or allowed hops.
            :param bool isShared: Specify whether these routes are shared. Shared routes can be used in more than one reservation.

            :rtype: EndPointConnectionInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetRoutesSolution'), ('reservationId', reservationId), ('sourceResourcesFullPath', sourceResourcesFullPath), ('targetResourcesFullPath', targetResourcesFullPath), ('mappingType', mappingType), ('maxHops', maxHops), ('isShared', isShared)]))

    def GenerateUtilizationReport(self, resourceFamilyName='', fromDate='', toDate='', resourceFullName='', resourceModelName='', includeChildResources=False, groupBy='', utilizationReportType=''):
        """
            Generates a utilization report for the specified resources. To generate a report for all resources, leave the resourceFullName and resourceModel parameters blank.

            :param str resourceFamilyName: Specify the name of the resource family.
            :param str fromDate: Specify the start time and date.
            :param str toDate: Specify the end time and date.
            :param str resourceFullName: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/ResourceName.
            :param str resourceModelName: Specify the resource model.
            :param bool includeChildResources: Specify whether to include child resources utilization.
            :param str groupBy: Specify how to group the utilization results: Resource, User, or Machine
            :param str utilizationReportType: Specify the report type: Lock or Mapping.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GenerateUtilizationReport'), ('resourceFamilyName', resourceFamilyName), ('fromDate', fromDate), ('toDate', toDate), ('resourceFullName', resourceFullName), ('resourceModelName', resourceModelName), ('includeChildResources', includeChildResources), ('groupBy', groupBy), ('utilizationReportType', utilizationReportType)]))

    def GetActiveTopologyNames(self):
        """
            Retrieves all active reserved topologies for the current (logged in) user.


            :rtype: TopologyListInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetActiveTopologyNames')]))

    def GetAllUsersDetails(self):
        """
            Retrieves all users and their settings.


            :rtype: UsersInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetAllUsersDetails')]))

    def GetAttributeValue(self, resourceFullPath='', attributeName=''):
        """
            Retrieves the value of the specified attribute

            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.
            :param str attributeName: Specify the attribute name.

            :rtype: AttributeValueInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetAttributeValue'), ('resourceFullPath', resourceFullPath), ('attributeName', attributeName)]))

    def GetCategoriesOfTopology(self, topologyPath=''):
        """
            Retrieves all categories of given topology.

            :param str topologyPath: Specify the topology name. Include the full path from the root to the topology, separated by slashes. For example: FolderName/Topologies/TopologyName.

            :rtype: CategoriesOfTopologyInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetCategoriesOfTopology'), ('topologyPath', topologyPath)]))

    def GetCurrentReservations(self, reservationOwner=''):
        """
            Retrieves current reservations for the specified owner. If an owner is not provided, this method retrieves all current reservations.

            :param str reservationOwner: Specify the user name of the reservation owner.

            :rtype: GetActiveReservationsResponseInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetCurrentReservations'), ('reservationOwner', reservationOwner)]))

    def GetDomainDetails(self, domainName=''):
        """
            Retrieves a domain's details including groups, topologies and resources associated with the specified domain.

            :param str domainName: Specify the name of the domain.

            :rtype: DomainInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetDomainDetails'), ('domainName', domainName)]))

    def GetFolderContent(self, fullPath='', showAllDomains=False):
        """
            Retrieves content for the specified path.

            :param str fullPath: Specify the full folder name. Include the full path from the root to a specific folder, separated by slashes. For example: ResourceFamilyFolder/ResourceModelFolder.
            :param bool showAllDomains: Show all domains associated with the logged in user.

            :rtype: ContentListInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetFolderContent'), ('fullPath', fullPath), ('showAllDomains', showAllDomains)]))

    def GetGroupDomains(self, groupName=''):
        """
            Retrieves all domains associated with a group.

            :param str groupName: Specify the name of the group.

            :rtype: GroupInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetGroupDomains'), ('groupName', groupName)]))

    def GetGroupsDetails(self):
        """
            Retrieves all groups, including members, roles and associated domains for each group.


            :rtype: GroupsInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetGroupsDetails')]))

    def GetLockedResources(self, user='', machine='', folderFullPath=''):
        """
            Retrieves locked resources for a specific user, a specific computer, or a specific folder. If none of these are specified, this method retrieves the list of locked resources for all users, on all machines, in all folders.

            :param str user: Specify a user name to retrieve locked resources for that user.
            :param str machine: Specify a machine name to retrieve locked resources for that computer.
            :param str folderFullPath: Specify the full folder name. Include the full path from the root to a specific folder, separated by slashes. For example: ResourceFamilyFolder/ResourceModelFolder.

            :rtype: ReservationInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetLockedResources'), ('user', user), ('machine', machine), ('folderFullPath', folderFullPath)]))

    def GetReservationDetails(self, reservationId=''):
        """
            Retrieves all details and parameters for a specified reservation, including its resources, routes and route segments, topologies, and reservation conflicts.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.

            :rtype: GetReservationDescriptionResponseInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetReservationDetails'), ('reservationId', reservationId)]))

    def GetReservationInputs(self, reservationId=''):
        """
            Retrieves all topology inputs for a specified reservation.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.

            :rtype: GetReservationInputsResponseInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetReservationInputs'), ('reservationId', reservationId)]))

    def GetReservationRemainingTime(self, reservationId=''):
        """
            Retrieves the number of minutes remaining until the end of a specified reservation. If the reservation is running overtime, the remaining time will be reported as -1 minutes.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.

            :rtype: GetReservationRemainingTimeInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetReservationRemainingTime'), ('reservationId', reservationId)]))

    def GetResourceAvailability(self, resourcesNames=[], showAllDomains=False):
        """
            Get resource availability for the resources.

            :param list[str] resourcesNames: Specify a list of resource names. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/ResourceName
            :param bool showAllDomains: Show all domains associated with the logged in user.

            :rtype: FindResourceListInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetResourceAvailability'), ('resourcesNames', resourcesNames), ('showAllDomains', showAllDomains)]))

    def GetResourceAvailabilityInTimeRange(self, resourcesNames=[], startTime='', endTime='', showAllDomains=False):
        """
            Get resource availability for the resources in the specified time range.

            :param list[str] resourcesNames: Specify a list of resource names. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/ResourceName
            :param str startTime: The start time of the reservation.
            :param str endTime: The end time of the reservation.
            :param bool showAllDomains: Show all domains associated with the logged in user.

            :rtype: FindResourceListInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetResourceAvailabilityInTimeRange'), ('resourcesNames', resourcesNames), ('startTime', startTime), ('endTime', endTime), ('showAllDomains', showAllDomains)]))

    def GetResourceCommands(self, resourceFullPath=''):
        """
            Retrieves driver commands and parameters for a specified resource.

            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.

            :rtype: ResourceCommandListInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetResourceCommands'), ('resourceFullPath', resourceFullPath)]))

    def GetServiceCommands(self, serviceName=''):
        """
            Retrieves driver commands and parameters for a specified service.

            :param str serviceName: Specify the service name. 

            :rtype: ResourceCommandListInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetServiceCommands'), ('serviceName', serviceName)]))

    def GetResourceConnectedCommands(self, resourceFullPath=''):
        """
            Gets commands which are added to the resource from connected resources such as power or virtualization.

            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.

            :rtype: ResourceCommandListInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetResourceConnectedCommands'), ('resourceFullPath', resourceFullPath)]))

    def GetResourceDetails(self, resourceFullPath='', showAllDomains=False):
        """
            Retrieves resource descriptions for the specified resource, and a matrix of all its associated attributes and attribute values.

            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.
            :param bool showAllDomains: Show all domains associated with the logged in user.

            :rtype: ResourceInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetResourceDetails'), ('resourceFullPath', resourceFullPath), ('showAllDomains', showAllDomains)]))

    def GetResourceList(self, folderFullPath=''):
        """
            Retrieves resources and resource values for the specified folder path.

            :param str folderFullPath: Specify the full folder name. Include the full path from the root to a specific folder, separated by slashes. For example: ResourceFamilyFolder/ResourceModelFolder.

            :rtype: ResourceListInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetResourceList'), ('folderFullPath', folderFullPath)]))

    def GetResourceLiveStatus(self, resourceFullPath=''):
        """
            Gets the live status of the resource.

            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA.

            :rtype: ResourceLiveStatusInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetResourceLiveStatus'), ('resourceFullPath', resourceFullPath)]))

    def GetReservationsLiveStatus(self, reservationsId=[]):
        """
            Gets the live status of the reservations.

            :param list[str] reservationsId: Specifies a string array that represents reservation unique identifiers.

            :rtype: ReservationLiveStatusInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetReservationsLiveStatus'), ('reservationsId', reservationsId)]))

    def GetResourceMappings(self, resources=[]):
        """
            Retrieves mappings for a list of one or more resources.

            :param list[str] resources: Specify a list of resources.

            :rtype: ResourceMappingsInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetResourceMappings'), ('resources', resources)]))

    def GetRouteSegments(self, resource=''):
        """
            Retrieves all the ports on the route from the selected endpoint to the target endpoint.

            :param str resource: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.

            :rtype: EndPointConnectionInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetRouteSegments'), ('resource', resource)]))

    def GetScheduledReservations(self, fromTime='', untilTime=''):
        """
            Retrieves all reservations scheduled between the specified start and end times.

            :param str fromTime: Specify from which time and date to search.
            :param str untilTime: Specify until which time and date to search.

            :rtype: GetReservationsInRangeResponseInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetScheduledReservations'), ('fromTime', fromTime), ('untilTime', untilTime)]))

    def GetServerDateAndTime(self):
        """
            Retrieves the server’s UTC date and time.


            :rtype: ServerTimeInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetServerDateAndTime')]))

    def GetTopologyCommands(self, reservationId=''):
        """
            [Deprecated] Retrieves driver commands and parameters for a specified reservation.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.

            :rtype: TopologyCommandListInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetTopologyCommands'), ('reservationId', reservationId)]))

    def GetEnvironmentCommands(self, reservationId=''):
        """
            Retrieves driver commands and parameters for a specified reservation.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.

            :rtype: EnvironmentCommandListInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetEnvironmentCommands'), ('reservationId', reservationId)]))

    def GetTopologyDetails(self, topologyFullPath=''):
        """
            Retrieves all resources and attributes associated with the specified topology.

            :param str topologyFullPath: Specify the full topology name. Include the full path from the root to the topology, separated by slashes. For example: FolderName/Topologies/TopologyName.

            :rtype: TopologyInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetTopologyDetails'), ('topologyFullPath', topologyFullPath)]))

    def GetTopologiesByCategory(self, categoryName='', categoryValue=''):
        """
            Retrives full topology path for each topology that contains given category name (and value if entered).

            :param str categoryName: Specify the category's name
            :param str categoryValue: Specify the category's value/sub category

            :rtype: TopologiesByCategoryInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetTopologiesByCategory'), ('categoryName', categoryName), ('categoryValue', categoryValue)]))

    def GetTopologyCategories(self):
        """
            Retrieves all root categories from 'Environment' catalog.


            :rtype: CategoryListInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetTopologyCategories')]))

    def GetUserDetails(self, username=''):
        """
            Retrieves the specified user's configuration settings and associated domains.

            :param str username: Specify the name of the user.

            :rtype: UserInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetUserDetails'), ('username', username)]))

    def GetAbstractTemplateList(self):
        """
            Retrieve a list of abstract templates.


            :rtype: AbstractTemplateShortInfoList
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetAbstractTemplateList')]))

    def GetServices(self, categoryName='', serviceName=''):
        """
            Retrieve a list of services and their attributes.

            :param str categoryName: The name of the category of the services you want to receive.
            :param str serviceName: The name of the service you want to receive.

            :rtype: ServicesListInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetServices'), ('categoryName', categoryName), ('serviceName', serviceName)]))

    def GetReservationServicesPositions(self, reservationId=''):
        """
            Retrieves the x/y coordinates for all services in the reservation's diagram.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.

            :rtype: ReservationDiagramLayoutResponseInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetReservationServicesPositions'), ('reservationId', reservationId)]))

    def GetVlanAutoSelectFirstNumericFromRange(self, poolId='', reservationId='', ownerId='', isolation='', start=0, end=0):
        """
            Request to get the first available numeric vlan from given range

            :param str poolId: Specify the name of the vlan pool id.
            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str ownerId: Specify the owner id.
            :param str isolation: Specify the requested isolation level for the requested vlan.
            :param int start: Specify the requested vlan range start.
            :param int end: Specify the requested vlan range end.

            :rtype: VlanPoolSingleNumericInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetVlanAutoSelectFirstNumericFromRange'), ('poolId', poolId), ('reservationId', reservationId), ('ownerId', ownerId), ('isolation', isolation), ('start', start), ('end', end)]))

    def GetVlanSpecificNumericRange(self, poolId='', reservationId='', ownerId='', isolation='', start=0, end=0):
        """
            Request to get the specific numeric vlan range

            :param str poolId: Specify the name of the vlan pool id.
            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str ownerId: Specify the owner id.
            :param str isolation: Specify the requested isolation level for the requested vlan.
            :param int start: Specify the requested vlan range start.
            :param int end: Specify the requested vlan range end.

            :rtype: VlanPoolRangeNumericInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetVlanSpecificNumericRange'), ('poolId', poolId), ('reservationId', reservationId), ('ownerId', ownerId), ('isolation', isolation), ('start', start), ('end', end)]))

    def GetVlanSpecificNumeric(self, poolId='', reservationId='', ownerId='', isolation='', specificValue=0):
        """
            Request to get a specific numeric vlan

            :param str poolId: Specify the name of the vlan pool id.
            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str ownerId: Specify the owner id.
            :param str isolation: Specify the requested isolation level for the requested vlan.
            :param int specificValue: Specify the requested vlan.

            :rtype: VlanPoolSingleNumericInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'GetVlanSpecificNumeric'), ('poolId', poolId), ('reservationId', reservationId), ('ownerId', ownerId), ('isolation', isolation), ('specificValue', specificValue)]))

    def IncludeResource(self, resourceFullPath=''):
        """
            Includes a specified resource.

            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'IncludeResource'), ('resourceFullPath', resourceFullPath)]))

    def IncludeResources(self, resourcesFullPath=[]):
        """
            Includes the specified resources.

            :param list[str] resourcesFullPath: Specify a list of resource names. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/ResourceName

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'IncludeResources'), ('resourcesFullPath', resourcesFullPath)]))

    def LockResource(self, reservationId='', resourceFullPath=''):
        """
            Locks a specified resource.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'LockResource'), ('reservationId', reservationId), ('resourceFullPath', resourceFullPath)]))

    def LockResources(self, reservationId='', resourcesFullPath=[]):
        """
            Locks multiple resources.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param list[str] resourcesFullPath: Specify a list of resource names. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/ResourceName

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'LockResources'), ('reservationId', reservationId), ('resourcesFullPath', resourcesFullPath)]))

    def Logoff(self):
        """
            Logs out the current user.


            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'Logoff')]))

    def Logon(self, username='', password='', domainName='Global'):
        """
            Logs in a user. If no user is specified, this method logs in the current user. If no domain is specified, this method logs the user in to the global (default) domain.

            :param str username: Username to logon with.
            :param str password: Specify the user’s login password.
            :param str domainName: Specify the name of the domain. If no domain is specified, it logs the user in to the global (default) domain.

            :rtype: LogonResponseInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'Logon'), ('username', username), ('password', password), ('domainName', domainName)]))

    def LogoutTNSession(self, reservationId='', resourceFullPath='', consolePortsFullPath=[], baudRate=0):
        """
            Logs the user out from a console port TN session.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.
            :param list[str] consolePortsFullPath: Specify a list of console ports according to their location in the Resource Explorer. Include the full path from the root to each console port, separated by slashes. For example: Console/Ports/PortName.
            :param int baudRate: Specify the baud rate to apply to the ports.

            :rtype: CommandExecutionCompletedResultInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'LogoutTNSession'), ('reservationId', reservationId), ('resourceFullPath', resourceFullPath), ('consolePortsFullPath', consolePortsFullPath), ('baudRate', baudRate)]))

    def MapPorts(self, sourcePort='', destinationPort='', mappingType=''):
        """
            Maps a pair of ports on a physical (L1) switch.

            :param str sourcePort: Specify the source port.
            :param str destinationPort: Specify the destination port.
            :param str mappingType: Specify bidirectional or unidirectional as the mapping type.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'MapPorts'), ('sourcePort', sourcePort), ('destinationPort', destinationPort), ('mappingType', mappingType)]))

    def PowerCycleResource(self, reservationId='', resourceFullPath='', powerPortsFullPath=[], delay=0):
        """
            Cycles the power options for resource power ports.

            :param str reservationId: Specify the reservation’s unique identifier. Admin users may leave this parameter blank to perform power operations on excluded resources.
            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.
            :param list[str] powerPortsFullPath: Specify the list of power ports to use in this operation. Include the full path from the root resource to each power port, separated by slashes. For example: Switch20/Blade5/PowerPort1. Leave blank to perform the power operation on all of the specified resource’s power ports.
            :param float delay: Specify the number of seconds to delay between each power cycle.

            :rtype: CommandExecutionCompletedResultInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'PowerCycleResource'), ('reservationId', reservationId), ('resourceFullPath', resourceFullPath), ('powerPortsFullPath', powerPortsFullPath), ('delay', delay)]))

    def PowerOffResource(self, reservationId='', resourceFullPath='', powerPortsFullPath=[]):
        """
            Powers off specified power ports.

            :param str reservationId: Specify the reservation’s unique identifier. Admin users may leave this parameter blank to perform power operations on excluded resources.
            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.
            :param list[str] powerPortsFullPath: Specify the list of power ports to use in this operation. Include the full path from the root resource to each power port, separated by slashes. For example: Switch20/Blade5/PowerPort1. Leave blank to perform the power operation on all of the specified resource’s power ports.

            :rtype: CommandExecutionCompletedResultInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'PowerOffResource'), ('reservationId', reservationId), ('resourceFullPath', resourceFullPath), ('powerPortsFullPath', powerPortsFullPath)]))

    def PowerOnResource(self, reservationId='', resourceFullPath='', powerPortsFullPath=[]):
        """
            Powers on resource power ports.

            :param str reservationId: Specify the reservation’s unique identifier. Admin users may leave this parameter blank to perform power operations on excluded resources.
            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.
            :param list[str] powerPortsFullPath: Specify the list of power ports to use in this operation. Include the full path from the root resource to each power port, separated by slashes. For example: Switch20/Blade5/PowerPort1. Leave blank to perform the power operation on all of the specified resource’s power ports.

            :rtype: CommandExecutionCompletedResultInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'PowerOnResource'), ('reservationId', reservationId), ('resourceFullPath', resourceFullPath), ('powerPortsFullPath', powerPortsFullPath)]))

    def RemoveAttributeRestrictedValues(self, removeAttributeRestrictionRequests=[]):
        """
            remove attribute restrictions from family/model

            :param list[RemoveRestrictionRequest] removeAttributeRestrictionRequests: Attribute restrictions to remove".

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'RemoveAttributeRestrictedValues'), ('removeAttributeRestrictionRequests', CommonAPIRequest.toContainer(removeAttributeRestrictionRequests))]))

    def RecheckConflicts(self, reservationId=''):
        """
            Updates the list of available resources for a reservation.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'RecheckConflicts'), ('reservationId', reservationId)]))

    def ReleaseResourcesFromReservation(self, reservationId='', resourcesFullPath=[]):
        """
            Releases occupied testing resources that would not otherwise be available until the end of the current reservation.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param list[str] resourcesFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'ReleaseResourcesFromReservation'), ('reservationId', reservationId), ('resourcesFullPath', resourcesFullPath)]))

    def ReleaseTopologyResources(self, reservationId='', topologyFullPath=''):
        """
            Releases resources used in topology. A reservation will not end until all used resources are released.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str topologyFullPath: Specify the full topology name. Include the full path from the root to the topology, separated by slashes. For example: FolderName/Topologies/TopologyName.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'ReleaseTopologyResources'), ('reservationId', reservationId), ('topologyFullPath', topologyFullPath)]))

    def ReloadTopology(self, reservationId='', topologyFullPath=''):
        """
            Removes and adds the specified topology back to the reservation, after re-evaluating it and all its resources.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str topologyFullPath: Specify the full topology name. Include the full path from the root to the topology, separated by slashes. For example: FolderName/Topologies/TopologyName.

            :rtype: ReserveTopologyResponseInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'ReloadTopology'), ('reservationId', reservationId), ('topologyFullPath', topologyFullPath)]))

    def RemoveGroupsFromDomain(self, domainName='', groupNames=[]):
        """
            Remove groups from a domain.

            :param str domainName: Specify the name of the domain.
            :param list[str] groupNames: Specify an array of one or more groups.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'RemoveGroupsFromDomain'), ('domainName', domainName), ('groupNames', groupNames)]))

    def RemovePermittedUsersFromReservation(self, reservationId='', usernames=[]):
        """
            Remove one or more permitted users from the specified reservation.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param list[str] usernames: List of permitted users to remove from the reservation.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'RemovePermittedUsersFromReservation'), ('reservationId', reservationId), ('usernames', usernames)]))

    def RemoveResourcesFromDomain(self, domainName='', resourcesNames=[]):
        """
            Remove resources from a domain.

            :param str domainName: Specify the name of the domain.
            :param list[str] resourcesNames: Specify a list of resource names. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/ResourceName

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'RemoveResourcesFromDomain'), ('domainName', domainName), ('resourcesNames', resourcesNames)]))

    def RemoveResourcesFromReservation(self, reservationId='', resourcesFullPath=[]):
        """
            Unlocks and removes resources from a reservation.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param list[str] resourcesFullPath: Specify a list of resource names. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/ResourceName

            :rtype: ReserveResourcesResponseInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'RemoveResourcesFromReservation'), ('reservationId', reservationId), ('resourcesFullPath', resourcesFullPath)]))

    def RemoveConnectorsFromReservation(self, reservationId='', endpoints=[]):
        """
            Removes the mapped connector between given end points.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param list[str] endpoints: The list of removed endpoints.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'RemoveConnectorsFromReservation'), ('reservationId', reservationId), ('endpoints', CommonAPIRequest.toContainer(endpoints))]))

    def RemoveRoutesFromReservation(self, reservationId='', endpoints=[], mappingType=''):
        """
            Disconnects a list of endpoints and removes the mapped route between them. Will only disconnect endpoints using resources reserved to the logged-in user .

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param list[str] endpoints: The list of removed endpoints.
            :param str mappingType: Specify bidirectional or unidirectional as the mapping type.

            :rtype: EndPointConnectionInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'RemoveRoutesFromReservation'), ('reservationId', reservationId), ('endpoints', CommonAPIRequest.toContainer(endpoints)), ('mappingType', mappingType)]))

    def RemoveTopologiesFromDomain(self, domainName='', topologyNames=[]):
        """
            Removes a list of one or more topologies from a domain.

            :param str domainName: Specify the name of the domain.
            :param list[str] topologyNames: Specify a list of topology names. Include the full path from the root to the topology, separated by slashes. For example: FolderName/Topologies/TopologyName.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'RemoveTopologiesFromDomain'), ('domainName', domainName), ('topologyNames', topologyNames)]))

    def RemoveUsersFromGroup(self, usernames=[], groupName=''):
        """
            Removes a list of one or more users from the specified group.

            :param list[str] usernames: Specify an array of one or more users.
            :param str groupName: Specify the name of the group.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'RemoveUsersFromGroup'), ('usernames', usernames), ('groupName', groupName)]))

    def RemoveTopologyCategory(self, topologyFullPath='', categoryName=''):
        """
            Removes a category from given topology.

            :param str topologyFullPath: Specify the topology we want to remove the given category from.
            :param str categoryName: Specify the category's name which we want to remove.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'RemoveTopologyCategory'), ('topologyFullPath', topologyFullPath), ('categoryName', categoryName)]))

    def RenameResource(self, resourceFullPath='', resourceName=''):
        """
            Renames the specified resource.

            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.
            :param str resourceName: Specify a new resource name.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'RenameResource'), ('resourceFullPath', resourceFullPath), ('resourceName', resourceName)]))

    def ResetResourceDriver(self, reservationId='', resourceFullPath=''):
        """
            Cancel the currently executing command, remove all pending command executions and reset the driver to its initial state.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.

            :rtype: CommandExecutionCompletedResultInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'ResetResourceDriver'), ('reservationId', reservationId), ('resourceFullPath', resourceFullPath)]))

    def RemoveAppFromReservation(self, reservationId='', appName=''):
        """
            Remove app resource to existing reservation.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str appName: Specify the app name.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'RemoveAppFromReservation'), ('reservationId', reservationId), ('appName', appName)]))

    def RemoveServicesFromReservation(self, reservationId='', services=[]):
        """
            Remove services and apps from existing reservation.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param list[str] services: List of aliases. This list should contain the aliases for both the services and apps that should be removed.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'RemoveServicesFromReservation'), ('reservationId', reservationId), ('services', services)]))

    def SaveReservationAsTopology(self, reservationId='', folderFullPath='', topologyName='', includeInactiveRoutes=False):
        """
            Creates a topology from an existing reservation. Leave the folder path blank to save the topology directly under the root.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str folderFullPath: Full container folder path where the new topology will be saved. leaving the folder path empty will try saving the topology under the root.  For example: FolderName/FolderNameA.
            :param str topologyName: Specify the new name for the new topology.
            :param bool includeInactiveRoutes: Include disconnected routes in the created topology

            :rtype: TopologyInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'SaveReservationAsTopology'), ('reservationId', reservationId), ('folderFullPath', folderFullPath), ('topologyName', topologyName), ('includeInactiveRoutes', includeInactiveRoutes)]))

    def SecureLogon(self, token='', domainName='Global'):
        """
            Logs in a user with a token. If no domain is specified, this method logs the user in to the global (default) domain.

            :param str token: Token to logon with.
            :param str domainName: Specify the name of the domain. If no domain is specified, it logs the user in to the global (default) domain.

            :rtype: LogonResponseInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'SecureLogon'), ('token', token), ('domainName', domainName)]))

    def SetAttributeValue(self, resourceFullPath='', attributeName='', attributeValue=''):
        """
            Sets the value of the specified attribute.

            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.
            :param str attributeName: Specify the attribute name.
            :param str attributeValue: Specify the attribute’s value.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'SetAttributeValue'), ('resourceFullPath', resourceFullPath), ('attributeName', attributeName), ('attributeValue', attributeValue)]))

    def SetAttributesValues(self, resourcesAttributesUpdateRequests=[]):
        """
            Sets new attribute values for the specified resources.

            :param list[ResourceAttributesUpdateRequest] resourcesAttributesUpdateRequests: Specify a matrix of resources, attribute names, and new attribute values (up to 10000 rows). For example: {['ResourceFullName', 'AttributeName','AttributeValue';'ResourceFullName2', 'AttributeName2','AttributeValue2']}.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'SetAttributesValues'), ('resourcesAttributesUpdateRequests', CommonAPIRequest.toContainer(resourcesAttributesUpdateRequests))]))

    def SetBaudRate(self, reservationId='', resourceFullPath='', consolePortsFullPath=[], baudRate=0):
        """
            Sets the baud rate for one or more console ports.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.
            :param list[str] consolePortsFullPath: Specify a list of console ports according to their location in the Resource Explorer. Include the full path from the root to each console port, separated by slashes. For example: Console/Ports/PortName.
            :param int baudRate: Specify the baud rate to apply to the ports.

            :rtype: CommandExecutionCompletedResultInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'SetBaudRate'), ('reservationId', reservationId), ('resourceFullPath', resourceFullPath), ('consolePortsFullPath', consolePortsFullPath), ('baudRate', baudRate)]))

    def SetConsoleForXModem(self, reservationId='', resourceFullPath='', consolePortsFullPath=[], baudRate=0):
        """
            Sets one or more consoles for Xmodem.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.
            :param list[str] consolePortsFullPath: Specify a list of console ports according to their location in the Resource Explorer. Include the full path from the root to each console port, separated by slashes. For example: Console/Ports/PortName.
            :param int baudRate: Specify the baud rate to apply to the ports.

            :rtype: CommandExecutionCompletedResultInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'SetConsoleForXModem'), ('reservationId', reservationId), ('resourceFullPath', resourceFullPath), ('consolePortsFullPath', consolePortsFullPath), ('baudRate', baudRate)]))

    def SetResourceLiveStatus(self, resourceFullName='', liveStatusName='', additionalInfo=''):
        """
            Sets the live status of the resource

            :param str resourceFullName: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA.
            :param str liveStatusName: Resource live status name
            :param str additionalInfo: Resource live status additional info

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'SetResourceLiveStatus'), ('resourceFullName', resourceFullName), ('liveStatusName', liveStatusName), ('additionalInfo', additionalInfo)]))

    def SetReservationLiveStatus(self, reservationId='', liveStatusName='', additionalInfo=''):
        """
            Sets the live status of the reservation

            :param str reservationId: Specifies the string that represents the reservation’s unique identifier.
            :param str liveStatusName: Reservation live status name
            :param str additionalInfo: Reservation live status additional info

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'SetReservationLiveStatus'), ('reservationId', reservationId), ('liveStatusName', liveStatusName), ('additionalInfo', additionalInfo)]))

    def SetResourceSharedState(self, reservationId='', resourcesFullName=[], isShared=False):
        """
            Sets the resource sharing state.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param list[str] resourcesFullName: Specify a list of resource names. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/ResourceName
            :param bool isShared: Specify whether to allow sharing of the resource.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'SetResourceSharedState'), ('reservationId', reservationId), ('resourcesFullName', resourcesFullName), ('isShared', isShared)]))

    def SetRouteAttributes(self, reservationId='', sourceResourceFullPath='', targetResourceFullPath='', applyChangesTo='', attributeRequests=[]):
        """
            Sets attributes and associated values for a specified route.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str sourceResourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.
            :param str targetResourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.
            :param str applyChangesTo: Specify on which resources to apply the attribute changes: Source/Target/All.Source refers to the resource connected to the source endpoint of the route. Target refers to the resource connected to the target endpoint of the route. All encompasses all route resources.
            :param list[str] attributeRequests: Specify an array of attributes and associated attribute values.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'SetRouteAttributes'), ('reservationId', reservationId), ('sourceResourceFullPath', sourceResourceFullPath), ('targetResourceFullPath', targetResourceFullPath), ('applyChangesTo', applyChangesTo), ('attributeRequests', attributeRequests)]))

    def SetRouteAttributesViaAlias(self, reservationId='', routeAlias='', applyChangesTo='', attributeRequests=[]):
        """
            Sets attributes and associated values for a route specified via its alias.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str routeAlias: Specify the route’s alias.
            :param str applyChangesTo: Specify on which resources to apply the attribute changes: Source/Target/All.Source refers to the resource connected to the source endpoint of the route. Target refers to the resource connected to the target endpoint of the route. All encompasses all route resources.
            :param list[str] attributeRequests: Specify an array of attributes and associated attribute values.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'SetRouteAttributesViaAlias'), ('reservationId', reservationId), ('routeAlias', routeAlias), ('applyChangesTo', applyChangesTo), ('attributeRequests', attributeRequests)]))

    def SetConnectorAttributes(self, reservationId='', sourceResourceFullName='', targetResourceFullName='', attributeRequests=[]):
        """
            Sets attributes and associated values for a specified connector.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str sourceResourceFullName: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.
            :param str targetResourceFullName: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.
            :param list[AttributeNameValue] attributeRequests: Specify a matrix of attributes and associated attribute values.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'SetConnectorAttributes'), ('reservationId', reservationId), ('sourceResourceFullName', sourceResourceFullName), ('targetResourceFullName', targetResourceFullName), ('attributeRequests', CommonAPIRequest.toContainer(attributeRequests))]))

    def SetConnectorAttributesViaAlias(self, reservationId='', connectorAlias='', attributeRequests=[]):
        """
            Sets attributes and associated values for a connector specified via its alias.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str connectorAlias: Specify the connector’s alias.
            :param list[AttributeNameValue] attributeRequests: Specify a matrix of attributes and associated attribute values.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'SetConnectorAttributesViaAlias'), ('reservationId', reservationId), ('connectorAlias', connectorAlias), ('attributeRequests', CommonAPIRequest.toContainer(attributeRequests))]))

    def SetGroupDomainPermissions(self, domainName='', groupName='', viewOnly=False):
        """
            Set the permission level of a group in domain.

            :param str domainName: Specify the name of the domain.
            :param str groupName: Specify the group name.
            :param bool viewOnly: Specify if the group should be have view only permissions.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'SetGroupDomainPermissions'), ('domainName', domainName), ('groupName', groupName), ('viewOnly', viewOnly)]))

    def SetConnectorsInReservation(self, reservationId='', connectors=[]):
        """
            Adds connectors between source and target or update existing ones.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param list[SetConnectorRequest] connectors: List of connectors to set in the reservation. For example: {['SourceResourceFullPath', 'TargetResourceFullPath', 'Direction', 'Alias';]}.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'SetConnectorsInReservation'), ('reservationId', reservationId), ('connectors', CommonAPIRequest.toContainer(connectors))]))

    def SetTopologyCategory(self, topologyFullPath='', categoryName='', categoryValue=''):
        """
            Set a category to given topology

            :param str topologyFullPath: Specify the topology we want to set the given category to
            :param str categoryName: Specify the category's name which we want to set
            :param str categoryValue: Specify the category's value

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'SetTopologyCategory'), ('topologyFullPath', topologyFullPath), ('categoryName', categoryName), ('categoryValue', categoryValue)]))

    def SyncResourceFromDevice(self, resourceFullPath=''):
        """
            Synchronizes the specified resource with current device settings and mappings.

            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'SyncResourceFromDevice'), ('resourceFullPath', resourceFullPath)]))

    def SyncResourceToDevice(self, resourceFullPath=''):
        """
            Updates device settings and mappings from the specified resource.

            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'SyncResourceToDevice'), ('resourceFullPath', resourceFullPath)]))

    def SetReservationResourcePosition(self, reservationId='', resourceFullName='', x=0, y=0):
        """
            Sets the location of a specified resource in the reservation diagram.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str resourceFullName: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/ResourceName.
            :param float x: Specify the x coordinate of the resource's top left corner.
            :param float y: Specify the y coordinate of the resource's top left corner.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'SetReservationResourcePosition'), ('reservationId', reservationId), ('resourceFullName', resourceFullName), ('x', x), ('y', y)]))

    def SetServiceDriver(self, serviceName='', driverName=''):
        """
            Sets the driver for a specified service model, if empty, removes its driver.

            :param str serviceName: Specify the name of the service model.
            :param str driverName: Specify the name of the driver.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'SetServiceDriver'), ('serviceName', serviceName), ('driverName', driverName)]))

    def SetServiceLiveStatus(self, reservationId='', serviceAlias='', liveStatusName='', additionalInfo=''):
        """
            Sets the live status of a service

            :param str reservationId: Specify the string that represents the reservation's unique identifier.
            :param str serviceAlias: Specify the string that represents the service's alias.
            :param str liveStatusName: Resource live status name
            :param str additionalInfo: Resource live status additional info

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'SetServiceLiveStatus'), ('reservationId', reservationId), ('serviceAlias', serviceAlias), ('liveStatusName', liveStatusName), ('additionalInfo', additionalInfo)]))

    def SetReservationServicePosition(self, reservationId='', serviceAlias='', x=0, y=0):
        """
            Sets the location of a specified service in the reservation diagram.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str serviceAlias: Specify the alias of the service.
            :param float x: Specify the x coordinate of the resource's top left corner.
            :param float y: Specify the y coordinate of the resource's top left corner.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'SetReservationServicePosition'), ('reservationId', reservationId), ('serviceAlias', serviceAlias), ('x', x), ('y', y)]))

    def SetServiceAttributesValues(self, reservationId='', serviceAlias='', attributeRequests=[]):
        """
            Sets attributes and associated values for a specified resource.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str serviceAlias: Specify the service name.
            :param list[AttributeNameValue] attributeRequests: Specify a matrix of attributes and associated attribute values.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'SetServiceAttributesValues'), ('reservationId', reservationId), ('serviceAlias', serviceAlias), ('attributeRequests', CommonAPIRequest.toContainer(attributeRequests))]))

    def TerminateReservation(self, reservationId=''):
        """
            Terminates the specified reservation if the reservation is in a state of teardown.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'TerminateReservation'), ('reservationId', reservationId)]))

    def UnlockResource(self, reservationId='', resourceFullPath=''):
        """
            Unlocks the specified resource.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'UnlockResource'), ('reservationId', reservationId), ('resourceFullPath', resourceFullPath)]))

    def UnlockResources(self, reservationId='', resourcesFullPath=[]):
        """
            Unlocks multiple resources.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param list[str] resourcesFullPath: Specify a list of resource names. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/ResourceName

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'UnlockResources'), ('reservationId', reservationId), ('resourcesFullPath', resourcesFullPath)]))

    def UnMapPorts(self, portA='', portB=''):
        """
            Removes existing mapping between a pair of physical (L1) switch ports.

            :param str portA: Specify the source port. (i.e. Folder1/Chassis1/Blade1/Port1).
            :param str portB: Specify the destination port. (i.e. Folder1/Chassis1/Blade1/Port1).

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'UnMapPorts'), ('portA', portA), ('portB', portB)]))

    def UpdateConnectorAliasInReservation(self, reservationId='', sourceResourceFullName='', targetResourceFullName='', direction='', alias=''):
        """
            Sets alias for a specified connector.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str sourceResourceFullName: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.
            :param str targetResourceFullName: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.
            :param str direction: Specify bidirectional or unidirectional as the connector direction.
            :param str alias: Specify the connector’s alias.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'UpdateConnectorAliasInReservation'), ('reservationId', reservationId), ('sourceResourceFullName', sourceResourceFullName), ('targetResourceFullName', targetResourceFullName), ('direction', direction), ('alias', alias)]))

    def UpdateConnectionWeight(self, resourceAFullPath='', resourceBFullPath='', weight=0):
        """
            Sets a weight score on a physical connection between two resources. Weights are used to optimize route resolution in physical switch scenarios.

            :param str resourceAFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.
            :param str resourceBFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.
            :param int weight: Specify a number to represent the connection weight between the specified resources.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'UpdateConnectionWeight'), ('resourceAFullPath', resourceAFullPath), ('resourceBFullPath', resourceBFullPath), ('weight', weight)]))

    def UpdateDomainTopologiesFolder(self, domainName='', topologiesFolder=''):
        """
            Update the domain’s topologies folder.

            :param str domainName: Specify the name of the domain.
            :param str topologiesFolder: Specify the topology name. Include the full path from the root to the topology, separated by slashes. For example: FolderName/Topologies/TopologyName.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'UpdateDomainTopologiesFolder'), ('domainName', domainName), ('topologiesFolder', topologiesFolder)]))

    def UnarchiveDomain(self, domainName=''):
        """
            Unarchive a domain. New reservation can be created.

            :param str domainName: Specify the name of the domain.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'UnarchiveDomain'), ('domainName', domainName)]))

    def UpdateGroup(self, groupName='', newName='', description='', groupRole=''):
        """
            Modifies the group name and description.

            :param str groupName: Specify the name of the group.
            :param str newName: Specify the new group name.
            :param str description: Provide a short description of the group.
            :param str groupRole: Specify the role of the group, possible values: External, Regular, DomainAdmin or Ignore (to keep the current role).

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'UpdateGroup'), ('groupName', groupName), ('newName', newName), ('description', description), ('groupRole', groupRole)]))

    def UpdatePhysicalConnection(self, resourceAFullPath='', resourceBFullPath='', overrideExistingConnections=True):
        """
            Define a physical connection (cable link) between two resources.

            :param str resourceAFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.
            :param str resourceBFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1. You may leave this parameter blank if you wish to disconnect the existing source resource connection.
            :param bool overrideExistingConnections: Overriding existing connections will automatically remove existing physical connection if they conflict with the requested new connections. If set to 'No', an error message will be displayed if any port is already connected and the operation will be cancelled.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'UpdatePhysicalConnection'), ('resourceAFullPath', resourceAFullPath), ('resourceBFullPath', resourceBFullPath), ('overrideExistingConnections', overrideExistingConnections)]))

    def UpdatePhysicalConnections(self, physicalConnectionUpdateRequest=[], overrideExistingConnections=True):
        """
            Define physical connections (cable links) between resources.

            :param list[PhysicalConnectionUpdateRequest] physicalConnectionUpdateRequest: Specify a matrix of physical connections to update. For example: {['ResourceA','ResourceB';'ResourceC',ResourceD']}
            :param bool overrideExistingConnections: Overriding existing connections will automatically remove existing physical connection if they conflict with the requested new connections. If set to 'No', an error message will be displayed if any port is already connected and the operation will be cancelled.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'UpdatePhysicalConnections'), ('physicalConnectionUpdateRequest', CommonAPIRequest.toContainer(physicalConnectionUpdateRequest)), ('overrideExistingConnections', overrideExistingConnections)]))

    def UpdateReservationDescription(self, reservationId='', description=''):
        """
            Modifies the description for a specified reservation.

            :param str reservationId: Specify the reservation ID.
            :param str description: Provide an updated description of the reservation. This text will replace the current description.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'UpdateReservationDescription'), ('reservationId', reservationId), ('description', description)]))

    def UpdateReservationGlobalInputs(self, reservationId='', globalInputs=[]):
        """
            Updates the unlinked global inputs in a specified reservation.

            :param str reservationId: Specify the reservation ID.
            :param list[UpdateTopologyGlobalInputsRequest] globalInputs: Global inputs associated with the specified topology. For example: {['Input Name', 'Value';]}.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'UpdateReservationGlobalInputs'), ('reservationId', reservationId), ('globalInputs', CommonAPIRequest.toContainer(globalInputs))]))

    def UpdateResourceAddress(self, resourceFullPath='', resourceAddress=''):
        """
            Modifies the address for a specified resource.

            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.
            :param str resourceAddress: Specify the resource’s new address.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'UpdateResourceAddress'), ('resourceFullPath', resourceFullPath), ('resourceAddress', resourceAddress)]))

    def UpdateResourceDescription(self, resourceFullPath='', resourceDescription=''):
        """
            Modifies the description for a specified resource.

            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.
            :param str resourceDescription: Provide an updated description of the resource. This text will replace the current description.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'UpdateResourceDescription'), ('resourceFullPath', resourceFullPath), ('resourceDescription', resourceDescription)]))

    def UpdateResourceDriver(self, resourceFullPath='', driverName=''):
        """
            Updates the driver for a specified resource.

            :param str resourceFullPath: Specify the resource name. You can also include the full path from the root to the resource before the resource name, separated by slashes. For example: FolderName/RouterA/Port1.
            :param str driverName: Specify the name of the driver.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'UpdateResourceDriver'), ('resourceFullPath', resourceFullPath), ('driverName', driverName)]))

    def UpdateTopologyOwner(self, topologyName='', ownerName=''):
        """
            Update the topology owner.

            :param str topologyName: Specify the topology name. Include the full path from the root to the topology, separated by slashes. For example: FolderName/Topologies/TopologyName.
            :param str ownerName: Specify the topology owner.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'UpdateTopologyOwner'), ('topologyName', topologyName), ('ownerName', ownerName)]))

    def UpdateTopologyDriver(self, topologyFullPath='', driverName=''):
        """
            Update the topology driver.

            :param str topologyFullPath: Specify the topology name. Include the full path from the root to the topology, separated by slashes. For example: FolderName/Topologies/TopologyName.
            :param str driverName: Specify the name of the driver. Leave empty to remove associated driver.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'UpdateTopologyDriver'), ('topologyFullPath', topologyFullPath), ('driverName', driverName)]))

    def UpdateUser(self, username='', email='', isActive=False):
        """
            Configures a user's email and activity settings.

            :param str username: The username of the user you want to update.
            :param str email: The new email address to update to.
            :param bool isActive: Grant or deny active access to the application.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'UpdateUser'), ('username', username), ('email', email), ('isActive', isActive)]))

    def UpdateUsersLimitations(self, userUpdateRequests=[]):
        """
            Update MaxConcurrentReservations and MaxReservationDuration.

            :param list[UserUpdateRequest] userUpdateRequests: List of Username, MaxConcurrentReservations and MaxReservationDuration of the users you wish to update.  For example: {['Username1','1','1';'Username2','12','10']}

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'UpdateUsersLimitations'), ('userUpdateRequests', CommonAPIRequest.toContainer(userUpdateRequests))]))

    def UpdateUserGroups(self, username='', groupsNames=[]):
        """
            Update an existing user's groups (replaces existing user's groups).

            :param str username: Specify the name of the user.
            :param list[str] groupsNames: Use this method to update a user's group memberships. Activating this method will replace the user's memberships with the specified list of groups.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'UpdateUserGroups'), ('username', username), ('groupsNames', groupsNames)]))

    def UpdateUserPassword(self, username='', password=''):
        """
            Changes a user's password.

            :param str username: Specify the name of the user.
            :param str password: Specify the user's new login password.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'UpdateUserPassword'), ('username', username), ('password', password)]))

    def UpdateRouteAliasesInReservation(self, reservationId='', routeAliases=[]):
        """
            Update route aliases in a reservation.

            :param str reservationId: Specifies the string that represents the reservation’s unique identifier.
            :param list[UpdateRouteAliasRequest] routeAliases: Specify a matrix of route source, route target and alias. For example: {['SourceResourceFullName', 'TargetFullName','Alias';'SourceResourceFullName2', 'TargetFullName2','Alias2']}.

            :rtype: EndPointConnectionInfo
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'UpdateRouteAliasesInReservation'), ('reservationId', reservationId), ('routeAliases', CommonAPIRequest.toContainer(routeAliases))]))

    def WriteMessageToReservationOutput(self, reservationId='', message=''):
        """
            Allows sending output to the command output window in a reservation.

            :param str reservationId: Specify the string that represents the reservation’s unique identifier.
            :param str message: Output message to the command output window.

            :rtype: str
        """
        return self.generateAPIRequest(OrderedDict([('method_name', 'WriteMessageToReservationOutput'), ('reservationId', reservationId), ('message', message)]))

