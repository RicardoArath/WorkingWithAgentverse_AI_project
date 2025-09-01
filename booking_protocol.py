from enum import Enum

from uagents import Agent, Bureau, Context, Model

class TableStatus(str, Enum):
    RESERVED = "reserved"
    FREE = "free"

class QueryTableRequest(Model):
    table_number: int
    
class QueryTableResponse(Model):
    status: TableStatus

class BookTableRequest(Model):
    table_number: int

class BookTableResponse(Model):
    success: bool

