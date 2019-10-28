-- Question1 starts from here. This is the complete answer, grouped into a single table. 

Select VariableName as "variable name",  VariableType as "variable type", Cardinality
From (
	Select Count(Distinct AppVersion) as 'Cardinality', 'AppVersion' as VariableName, 'Categorical' as VariableType
	From Malware_train
	Union all

	Select Count(Distinct Census_ActivationChannel) as 'Cardinality', 'Census_ActivationChannel' as VariableName, 'Categorical' as VariableType
	From Malware_train
	Union all

	Select Count(Distinct Census_ChassisTypeName) as 'Cardinality', 'Census_ChassisTypeName' as VariableName, 'Categorical' as VariableType
	From Malware_train
	Union all

	Select Count(Distinct Census_DeviceFamily) as 'Cardinality', 'Census_DeviceFamily' as VariableName, 'Categorical' as VariableType
	From Malware_train
	Union all

	Select Count(Distinct Census_FirmwareManufacturerIdentifier) as 'Cardinality', 'Census_FirmwareManufacturerIdentifier' as VariableName, 'Categorical' as VariableType
	From Malware_train
)ok

-- Question2 starts from here. Each part is done individually for each category.

Select
	AppVersion as Category,
	Count(1) as Frequency,
	Count(1)/(Select Count(AppVersion) From Malware_train)*100 as Percentage
From
	Malware_train
Group by
	AppVersion


Select
	Census_ActivationChannel as Category,
	Count(1) as Frequency,
	Count(1)/(Select Count(Census_ActivationChannel) From Malware_train)*100 as Percentage
From
	Malware_train
Group by
	Census_ActivationChannel


Select
	Census_ChassisTypeName as Category,
	Count(1) as Frequency,
	Count(1)/(Select Count(Census_ChassisTypeName) From Malware_train)*100 as Percentage
From
	Malware_train
Group by
	Census_ChassisTypeName


Select
	Census_DeviceFamily as Category,
	Count(1) as Frequency,
	Count(1)/(Select Count(Census_DeviceFamily) From Malware_train)*100 as Percentage
From
	Malware_train
Group by
	Census_DeviceFamily


Select
	Census_FirmwareManufacturerIdentifier as Category,
	Count(1) as Frequency,
	Count(1)/(Select Count(Census_FirmwareManufacturerIdentifier) From Malware_train)*100 as Percentage
From
	Malware_train
Group by
	Census_FirmwareManufacturerIdentifier