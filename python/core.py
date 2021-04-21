# Auto generated from core.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-04-14 16:48
# Schema: Alliance-Schema-Prototype-Core-Types
#
# id: https://github.com/alliance-genome/agr_persistent_schema/core.yaml
# description: Alliance Schema Prototype with LinkML
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml.utils.slot import Slot
from linkml.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml.utils.formatutils import camelcase, underscore, sfx
from linkml.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml.utils.curienamespace import CurieNamespace
from linkml.utils.metamodelcore import Bool, URIorCURIE, XSDDate
from linkml_model.types import Boolean, Date, String, Uriorcurie

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ENSEMBL = CurieNamespace('ENSEMBL', 'http://identifiers.org/ensembl/')
FB = CurieNamespace('FB', 'http://identifiers.org/fb/')
HGNC = CurieNamespace('HGNC', 'http://identifiers.org/hgnc/')
MGI = CurieNamespace('MGI', 'http://identifiers.org/mgi/')
RGD = CurieNamespace('RGD', 'http://identifiers.org/rgd/')
SGD = CurieNamespace('SGD', 'http://identifiers.org/sgd/')
WB = CurieNamespace('WB', 'http://identifiers.org/wb/')
ZFIN = CurieNamespace('ZFIN', 'http://identifiers.org/zfin/')
ALLIANCE = CurieNamespace('alliance', 'http://alliancegenome.org')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
FALDO = CurieNamespace('faldo', 'http://biohackathon.org/resource/faldo#')
GFF = CurieNamespace('gff', 'https://w3id.org/gff')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SKOS = CurieNamespace('skos', 'https://www.w3.org/TR/skos-reference/#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = ALLIANCE


# Types
class BiologicalSequence(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "biological sequence"
    type_model_uri = ALLIANCE.BiologicalSequence


# Class references



class Entity(YAMLRoot):
    """
    Root Biolink Model class for all things and informational relationships, real or imagined.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Entity
    class_class_curie: ClassVar[str] = "alliance:Entity"
    class_name: ClassVar[str] = "entity"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Entity


class NamedThing(Entity):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.NamedThing
    class_class_curie: ClassVar[str] = "alliance:NamedThing"
    class_name: ClassVar[str] = "named thing"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.NamedThing


class GenomicEntity(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GenomicEntity
    class_class_curie: ClassVar[str] = "alliance:GenomicEntity"
    class_name: ClassVar[str] = "genomic entity"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GenomicEntity


class Gene(NamedThing):
    """
    A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A
    gene locus may include regulatory regions, transcribed regions and/or other functional sequence regions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Gene
    class_class_curie: ClassVar[str] = "alliance:Gene"
    class_name: ClassVar[str] = "gene"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Gene


class Transcript(NamedThing):
    """
    An RNA synthesized on a DNA or RNA template by an RNA polymerase.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Transcript
    class_class_curie: ClassVar[str] = "alliance:Transcript"
    class_name: ClassVar[str] = "transcript"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Transcript


class Allele(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Allele
    class_class_curie: ClassVar[str] = "alliance:Allele"
    class_name: ClassVar[str] = "allele"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Allele


class Species(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Species
    class_class_curie: ClassVar[str] = "alliance:Species"
    class_name: ClassVar[str] = "species"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Species


@dataclass
class Association(Entity):
    """
    A typed association between two entities, supported by evidence
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Association
    class_class_curie: ClassVar[str] = "alliance:Association"
    class_name: ClassVar[str] = "association"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Association

    subject: Union[dict, NamedThing] = None
    predicate: str = None
    object: Union[dict, NamedThing] = None
    negated: Optional[Union[bool, Bool]] = None
    qualifiers: Optional[Union[dict, Entity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, NamedThing):
            self.subject = NamedThing()

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, NamedThing):
            self.object = NamedThing()

        if self.negated is not None and not isinstance(self.negated, Bool):
            self.negated = Bool(self.negated)

        if self.qualifiers is not None and not isinstance(self.qualifiers, Entity):
            self.qualifiers = Entity()

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=ALLIANCE.id, name="id", curie=ALLIANCE.curie('id'),
                   model_uri=ALLIANCE.id, domain=None, range=URIRef)

slots.date_produced = Slot(uri=ALLIANCE.date_produced, name="date_produced", curie=ALLIANCE.curie('date_produced'),
                   model_uri=ALLIANCE.date_produced, domain=NamedThing, range=Optional[Union[str, XSDDate]])

slots.release = Slot(uri=ALLIANCE.release, name="release", curie=ALLIANCE.curie('release'),
                   model_uri=ALLIANCE.release, domain=NamedThing, range=Optional[str])

slots.data_provider = Slot(uri=ALLIANCE.data_provider, name="data provider", curie=ALLIANCE.curie('data_provider'),
                   model_uri=ALLIANCE.data_provider, domain=NamedThing, range=Optional[Union[str, List[str]]])

slots.association_slot = Slot(uri=ALLIANCE.association_slot, name="association slot", curie=ALLIANCE.curie('association_slot'),
                   model_uri=ALLIANCE.association_slot, domain=Association, range=Optional[str])

slots.subject = Slot(uri=ALLIANCE.subject, name="subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.subject, domain=Association, range=Union[dict, NamedThing])

slots.object = Slot(uri=ALLIANCE.object, name="object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.object, domain=Association, range=Union[dict, NamedThing])

slots.predicate = Slot(uri=ALLIANCE.predicate, name="predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.predicate, domain=Association, range=str)

slots.description = Slot(uri=ALLIANCE.description, name="description", curie=ALLIANCE.curie('description'),
                   model_uri=ALLIANCE.description, domain=None, range=Optional[str])

slots.name = Slot(uri=ALLIANCE.name, name="name", curie=ALLIANCE.curie('name'),
                   model_uri=ALLIANCE.name, domain=None, range=Optional[str])

slots.cross_references = Slot(uri=ALLIANCE.cross_references, name="cross references", curie=ALLIANCE.curie('cross_references'),
                   model_uri=ALLIANCE.cross_references, domain=NamedThing, range=Optional[Union[str, List[str]]])

slots.symbol = Slot(uri=ALLIANCE.symbol, name="symbol", curie=ALLIANCE.curie('symbol'),
                   model_uri=ALLIANCE.symbol, domain=NamedThing, range=Optional[str])

slots.from_species = Slot(uri=ALLIANCE.from_species, name="from species", curie=ALLIANCE.curie('from_species'),
                   model_uri=ALLIANCE.from_species, domain=NamedThing, range=Optional[Union[dict, "Species"]])

slots.synonym = Slot(uri=ALLIANCE.synonym, name="synonym", curie=ALLIANCE.curie('synonym'),
                   model_uri=ALLIANCE.synonym, domain=NamedThing, range=Optional[Union[str, List[str]]])

slots.negated = Slot(uri=ALLIANCE.negated, name="negated", curie=ALLIANCE.curie('negated'),
                   model_uri=ALLIANCE.negated, domain=None, range=Optional[Union[bool, Bool]])

slots.qualifiers = Slot(uri=ALLIANCE.qualifiers, name="qualifiers", curie=ALLIANCE.curie('qualifiers'),
                   model_uri=ALLIANCE.qualifiers, domain=None, range=Optional[Union[dict, Entity]])

slots.synonyms = Slot(uri=ALLIANCE.synonyms, name="synonyms", curie=ALLIANCE.curie('synonyms'),
                   model_uri=ALLIANCE.synonyms, domain=None, range=Optional[str])

slots.type = Slot(uri=ALLIANCE.type, name="type", curie=ALLIANCE.curie('type'),
                   model_uri=ALLIANCE.type, domain=None, range=Optional[Union[str, URIorCURIE]])