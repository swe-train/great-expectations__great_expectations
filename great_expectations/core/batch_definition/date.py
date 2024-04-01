
from great_expectations.core.batch_definition.batch_definition_base import BatchDefinitionBase
from great_expectations.core.partitioners import PartitionerYearAndMonthAndDay


class Date(BatchDefinitionBase):
    column: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._partitioner = PartitionerYearAndMonthAndDay(column_name=self.column)
