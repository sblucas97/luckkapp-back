from marshmallow import Schema, fields

class PrizeSchema(Schema):
    id = fields.UUID(dump_only=True)
    name = fields.Str()
    description = fields.Str()
    img = fields.Str()
    amount = fields.Int()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()