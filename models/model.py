from marshmallow import fields
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()

class GetItems(db.Model):
    __tablename__ = 'magiccard'
    GathererId = db.Column(db.String(16), primary_key=True, nullable=False)
    Variation = db.Column(db.Integer, nullable=True)
    SearchName = db.Column(db.String, nullable=False)
    PtBRSearchName = db.Column(db.String, nullable=True)
    EnglishName = db.Column(db.String, nullable=False)
    PtBRName = db.Column(db.String, nullable=True)
    LinkName = db.Column(db.String, nullable=False)
    Color = db.Column(db.Integer, nullable=False)
    ManaCost = db.Column(db.String(128), nullable=True)
    CollectionNumber = db.Column(db.Integer, nullable=True)
    ConvertedManaCost = db.Column(db.Float, nullable=True)
    Rarity = db.Column(db.String(1), nullable=False)
    Rules = db.Column(db.String, nullable=False)
    FlavorText = db.Column(db.String, nullable=False)
    SuperTypes = db.Column(db.Integer, nullable=False)
    CardTypes = db.Column(db.Integer, nullable=False)
    UnseriousSubTypes = db.Column(db.String(128), nullable=True)
    Power = db.Column(db.String(4), nullable=True)
    Toughness = db.Column(db.String(4), nullable=True)
    Loyalty = db.Column(db.String(4), nullable=True)
    ExpansionId = db.Column(db.Integer, nullable=False)
    ArtistId = db.Column(db.Integer, nullable=False)
    FlipName = db.Column(db.String, nullable=True)
    FlipRules = db.Column(db.String, nullable=True)
    FlipSuperTypes = db.Column(db.Integer, nullable=True)
    FlipTypes = db.Column(db.Integer, nullable=True)
    FlipPower = db.Column(db.String(4), nullable=True)
    FlipToughness = db.Column(db.String(4), nullable=True)
    FlipGathererId = db.Column(db.String(16), nullable=True)
    SplitManaCost = db.Column(db.String(128), nullable=True)
    SplitConvertedManaCost = db.Column(db.Float(128), nullable=True)


    def __init__(self, GathererId, Variation, SearchName, PtBRSearchName, EnglishName, PtBRName,
                 LinkName, Color, ManaCost, CollectionNumber, ConvertedManaCost, Rarity, Rules,
                 FlavorText, SuperTypes, CardTypes, UnseriousSubTypes, Power, Toughness, Loyalty,
                 ExpansionId, ArtistId, FlipName, FlipRules, FlipSuperTypes, FlipTypes, FlipPower,
                 FlipToughness, FlipGathererId, SplitManaCost, SplitConvertedManaCost):

        self.GathererId = GathererId
        self.Variation = Variation
        self.SearchName = SearchName
        self.PtBRSearchName = PtBRSearchName
        self.EnglishName = EnglishName
        self.PtBRName = PtBRName
        self.LinkName = LinkName
        self.Color = Color
        self.ManaCost = ManaCost
        self.CollectionNumber = CollectionNumber
        self.ConvertedManaCost = ConvertedManaCost
        self.Rarity = Rarity
        self.Rules = Rules
        self.FlavorText = FlavorText
        self.SuperTypes = SuperTypes
        self.CardTypes = CardTypes
        self.UnseriousSubTypes = UnseriousSubTypes
        self.Power = Power
        self.Toughness = Toughness
        self.Loyalty = Loyalty
        self.ExpansionId = ExpansionId
        self.ArtistId = ArtistId
        self.FlipName = FlipName
        self.FlipRules = FlipRules
        self.FlipSuperTypes = FlipSuperTypes
        self.FlipTypes = FlipTypes
        self.FlipPower = FlipPower
        self.FlipToughness = FlipToughness
        self.FlipGathererId = FlipGathererId
        self.SplitManaCost = SplitManaCost
        self.SplitConvertedManaCost = SplitConvertedManaCost


class GetItemsSchema(ma.Schema):
    GathererId = fields.String()
    Variation = fields.Integer()
    SearchName = fields.String()
    PtBRSearchName = fields.String()
    EnglishName = fields.String()
    PtBRName = fields.String()
    LinkName = fields.String()
    Color = fields.Integer()
    ManaCost = fields.String()
    CollectionNumber = fields.Integer()
    ConvertedManaCost = fields.Float()
    Rarity = fields.String()
    Rules = fields.String()
    FlavorText = fields.String()
    SuperTypes = fields.Integer()
    CardTypes = fields.Integer()
    UnseriousSubTypes = fields.String()
    Power = fields.String()
    Toughness = fields.String()
    Loyalty = fields.String()
    ExpansionId = fields.Integer()
    ArtistId = fields.Integer()
    FlipName = fields.String()
    FlipRules = fields.String()
    FlipSuperTypes = fields.Integer()
    FlipTypes = fields.Integer()
    FlipPower = fields.String()
    FlipToughness = fields.String()
    FlipGathererId = fields.String()
    SplitManaCost = fields.String()
    SplitConvertedManaCost = fields.Float()
