from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.UUID(dump_only=True)
    full_name = fields.Str()
    password = fields.Str()
    city = fields.Str()
    phone = fields.Str()
    email = fields.Email()
    is_admin = fields.Bool()
    birthday = fields.Date()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()