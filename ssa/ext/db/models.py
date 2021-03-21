from ssa.ext.db import db

class Cloth(db.Model):
    __tablename__ = 'cloth'
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(255))


class Rarity(db.Model):
    __tablename__ = 'rarity'
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(255))


class Saint(db.Model):
    __tablename__ = 'saint'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    rarity_id = db.Column(db.ForeignKey('rarity.id'))
    hp = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    defense = db.Column(db.Integer)
    cdef = db.Column(db.Integer)
    pdef = db.Column(db.Integer)
    catk = db.Column(db.Integer)
    patk = db.Column(db.Integer)
    pcrit = db.Column(db.Integer)
    pcrit_level = db.Column(db.Integer)
    crit_rate = db.Column(db.Integer)
    avatar = db.Column(db.String(255))
    cloth_id = db.Column(db.ForeignKey('cloth.id'))
    cloth = db.relationship('Cloth')
    rarity = db.relationship('Rarity')


class SaintSkill(db.Model):
    __tablename__ = 'saint_skill'
    id = db.Column(db.Integer, primary_key=True)
    saint_id = db.Column(db.ForeignKey('saint.id'))
    img = db.Column(db.String(255))
    name = db.Column(db.String(255))
    desc = db.Column(db.Text)
    cost = db.Column(db.Integer)
    saint = db.relationship('Saint')
    skill_types = db.relationship('SkillType', secondary='saint_skill_type')


t_saint_skill_type = db.Table(
    'saint_skill_type', db.metadata,
    db.Column('saint_skill_id', db.ForeignKey('saint_skill.id'), primary_key=True, nullable=False),
    db.Column('skill_type_id', db.ForeignKey('skill_type.id'), primary_key=True, nullable=False)
)


class SkillType(db.Model):
    __tablename__ = 'skill_type'
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(255))
