# Auto generated from core.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-05-19 13:22
# Schema: Alliance-Schema-Prototype-Core
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
from . genomic import GeneGenomicLocation
from . reference import ReferenceId
from . resource import Resource
from linkml.utils.metamodelcore import Bool, URIorCURIE, XSDDate
from linkml_model.types import Boolean, Date, Integer, String, Uriorcurie

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ENSEMBL = CurieNamespace('ENSEMBL', 'http://identifiers.org/ensembl/')
FB = CurieNamespace('FB', 'http://identifiers.org/fb/')
HGNC = CurieNamespace('HGNC', 'http://identifiers.org/hgnc/')
MGI = CurieNamespace('MGI', 'http://identifiers.org/mgi/')
NLMID = CurieNamespace('NLMID', 'https://www.ncbi.nlm.nih.gov/nlmcatalog/?term=')
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
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'https://www.w3.org/TR/skos-reference/#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = ALLIANCE


# Types
class BiologicalSequence(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "biological_sequence"
    type_model_uri = ALLIANCE.BiologicalSequence


# Class references
class GenomicEntityId(URIorCURIE):
    pass


class TranscriptId(GenomicEntityId):
    pass


class GeneId(GenomicEntityId):
    pass


@dataclass
class GenomicEntity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GenomicEntity
    class_class_curie: ClassVar[str] = "alliance:GenomicEntity"
    class_name: ClassVar[str] = "GenomicEntity"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GenomicEntity

    id: Union[str, GenomicEntityId] = None
    taxon: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GenomicEntityId):
            self.id = GenomicEntityId(self.id)

        if self.taxon is not None and not isinstance(self.taxon, URIorCURIE):
            self.taxon = URIorCURIE(self.taxon)

        super().__post_init__(**kwargs)


@dataclass
class Transcript(GenomicEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Transcript
    class_class_curie: ClassVar[str] = "alliance:Transcript"
    class_name: ClassVar[str] = "Transcript"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Transcript

    id: Union[str, TranscriptId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, TranscriptId):
            self.id = TranscriptId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Gene(GenomicEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Gene
    class_class_curie: ClassVar[str] = "alliance:Gene"
    class_name: ClassVar[str] = "Gene"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Gene

    id: Union[str, GeneId] = None
    curie: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()
    secondary_identifiers: Optional[Union[str, List[str]]] = empty_list()
    cross_references: Optional[Union[str, List[str]]] = empty_list()
    genomic_locations: Optional[Union[Union[dict, GeneGenomicLocation], List[Union[dict, GeneGenomicLocation]]]] = empty_list()
    name: Optional[str] = None
    symbol: Optional[str] = None
    gene_synopsis: Optional[str] = None
    gene_synopsis_URL: Optional[str] = None
    type: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GeneId):
            self.id = GeneId(self.id)

        if self.curie is not None and not isinstance(self.curie, str):
            self.curie = str(self.curie)

        if self.synonyms is None:
            self.synonyms = []
        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms]
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        if self.secondary_identifiers is None:
            self.secondary_identifiers = []
        if not isinstance(self.secondary_identifiers, list):
            self.secondary_identifiers = [self.secondary_identifiers]
        self.secondary_identifiers = [v if isinstance(v, str) else str(v) for v in self.secondary_identifiers]

        if self.cross_references is None:
            self.cross_references = []
        if not isinstance(self.cross_references, list):
            self.cross_references = [self.cross_references]
        self.cross_references = [v if isinstance(v, str) else str(v) for v in self.cross_references]

        if self.genomic_locations is None:
            self.genomic_locations = []
        if not isinstance(self.genomic_locations, list):
            self.genomic_locations = [self.genomic_locations]
        self._normalize_inlined_slot(slot_name="genomic_locations", slot_type=GeneGenomicLocation, key_name="subject", inlined_as_list=True, keyed=False)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.symbol is not None and not isinstance(self.symbol, str):
            self.symbol = str(self.symbol)

        if self.gene_synopsis is not None and not isinstance(self.gene_synopsis, str):
            self.gene_synopsis = str(self.gene_synopsis)

        if self.gene_synopsis_URL is not None and not isinstance(self.gene_synopsis_URL, str):
            self.gene_synopsis_URL = str(self.gene_synopsis_URL)

        if self.type is not None and not isinstance(self.type, URIorCURIE):
            self.type = URIorCURIE(self.type)

        super().__post_init__(**kwargs)


class DiseaseAssociation(YAMLRoot):
    """
    Dummy disease association class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.DiseaseAssociation
    class_class_curie: ClassVar[str] = "alliance:DiseaseAssociation"
    class_name: ClassVar[str] = "DiseaseAssociation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.DiseaseAssociation


class PhenotypeAssociation(YAMLRoot):
    """
    Dummy phenotype association class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.PhenotypeAssociation
    class_class_curie: ClassVar[str] = "alliance:PhenotypeAssociation"
    class_name: ClassVar[str] = "PhenotypeAssociation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.PhenotypeAssociation


class Species(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Species
    class_class_curie: ClassVar[str] = "alliance:Species"
    class_name: ClassVar[str] = "Species"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Species


class Disease(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Disease
    class_class_curie: ClassVar[str] = "alliance:Disease"
    class_name: ClassVar[str] = "Disease"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Disease


class Phenotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Phenotype
    class_class_curie: ClassVar[str] = "alliance:Phenotype"
    class_name: ClassVar[str] = "Phenotype"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Phenotype


# Enumerations


# Slots
class slots:
    pass

slots.curie = Slot(uri=ALLIANCE.curie, name="curie", curie=ALLIANCE.curie('curie'),
                   model_uri=ALLIANCE.curie, domain=None, range=Optional[str])

slots.taxon = Slot(uri=ALLIANCE.taxon, name="taxon", curie=ALLIANCE.curie('taxon'),
                   model_uri=ALLIANCE.taxon, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.secondary_identifiers = Slot(uri=ALLIANCE.secondary_identifiers, name="secondary_identifiers", curie=ALLIANCE.curie('secondary_identifiers'),
                   model_uri=ALLIANCE.secondary_identifiers, domain=None, range=Optional[Union[str, List[str]]])

slots.gene_synopsis = Slot(uri=ALLIANCE.gene_synopsis, name="gene_synopsis", curie=ALLIANCE.curie('gene_synopsis'),
                   model_uri=ALLIANCE.gene_synopsis, domain=None, range=Optional[str])

slots.gene_synopsis_URL = Slot(uri=ALLIANCE.gene_synopsis_URL, name="gene_synopsis_URL", curie=ALLIANCE.curie('gene_synopsis_URL'),
                   model_uri=ALLIANCE.gene_synopsis_URL, domain=None, range=Optional[str])

slots.genomic_locations = Slot(uri=ALLIANCE.genomic_locations, name="genomic_locations", curie=ALLIANCE.curie('genomic_locations'),
                   model_uri=ALLIANCE.genomic_locations, domain=GenomicEntity, range=Optional[Union[Union[dict, GeneGenomicLocation], List[Union[dict, GeneGenomicLocation]]]])

slots.id = Slot(uri=ALLIANCE.id, name="id", curie=ALLIANCE.curie('id'),
                   model_uri=ALLIANCE.id, domain=None, range=URIRef)

slots.date_produced = Slot(uri=ALLIANCE.date_produced, name="date_produced", curie=ALLIANCE.curie('date_produced'),
                   model_uri=ALLIANCE.date_produced, domain=GenomicEntity, range=Optional[Union[str, XSDDate]])

slots.release = Slot(uri=ALLIANCE.release, name="release", curie=ALLIANCE.curie('release'),
                   model_uri=ALLIANCE.release, domain=None, range=Optional[str])

slots.data_provider = Slot(uri=ALLIANCE.data_provider, name="data_provider", curie=ALLIANCE.curie('data_provider'),
                   model_uri=ALLIANCE.data_provider, domain=None, range=Optional[Union[str, List[str]]])

slots.association_slot = Slot(uri=ALLIANCE.association_slot, name="association_slot", curie=ALLIANCE.curie('association_slot'),
                   model_uri=ALLIANCE.association_slot, domain=None, range=Optional[str])

slots.subject = Slot(uri=ALLIANCE.subject, name="subject", curie=ALLIANCE.curie('subject'),
                   model_uri=ALLIANCE.subject, domain=None, range=str)

slots.object = Slot(uri=ALLIANCE.object, name="object", curie=ALLIANCE.curie('object'),
                   model_uri=ALLIANCE.object, domain=None, range=str)

slots.predicate = Slot(uri=ALLIANCE.predicate, name="predicate", curie=ALLIANCE.curie('predicate'),
                   model_uri=ALLIANCE.predicate, domain=None, range=str)

slots.description = Slot(uri=ALLIANCE.description, name="description", curie=ALLIANCE.curie('description'),
                   model_uri=ALLIANCE.description, domain=None, range=Optional[str])

slots.name = Slot(uri=ALLIANCE.name, name="name", curie=ALLIANCE.curie('name'),
                   model_uri=ALLIANCE.name, domain=None, range=Optional[str])

slots.cross_references = Slot(uri=ALLIANCE.cross_references, name="cross_references", curie=ALLIANCE.curie('cross_references'),
                   model_uri=ALLIANCE.cross_references, domain=None, range=Optional[Union[str, List[str]]])

slots.symbol = Slot(uri=ALLIANCE.symbol, name="symbol", curie=ALLIANCE.curie('symbol'),
                   model_uri=ALLIANCE.symbol, domain=None, range=Optional[str])

slots.from_species = Slot(uri=ALLIANCE.from_species, name="from_species", curie=ALLIANCE.curie('from_species'),
                   model_uri=ALLIANCE.from_species, domain=None, range=Optional[Union[dict, Species]])

slots.synonyms = Slot(uri=ALLIANCE.synonyms, name="synonyms", curie=ALLIANCE.curie('synonyms'),
                   model_uri=ALLIANCE.synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.negated = Slot(uri=ALLIANCE.negated, name="negated", curie=ALLIANCE.curie('negated'),
                   model_uri=ALLIANCE.negated, domain=None, range=Optional[Union[bool, Bool]])

slots.qualifiers = Slot(uri=ALLIANCE.qualifiers, name="qualifiers", curie=ALLIANCE.curie('qualifiers'),
                   model_uri=ALLIANCE.qualifiers, domain=None, range=Optional[str])

slots.type = Slot(uri=ALLIANCE.type, name="type", curie=ALLIANCE.curie('type'),
                   model_uri=ALLIANCE.type, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.taxon_id = Slot(uri=ALLIANCE.taxon_id, name="taxon_id", curie=ALLIANCE.curie('taxon_id'),
                   model_uri=ALLIANCE.taxon_id, domain=None, range=Optional[int])

slots.references = Slot(uri=ALLIANCE.references, name="references", curie=ALLIANCE.curie('references'),
                   model_uri=ALLIANCE.references, domain=Resource, range=Optional[Union[Union[str, ReferenceId], List[Union[str, ReferenceId]]]])

slots.phenotype_associations = Slot(uri=ALLIANCE.phenotype_associations, name="phenotype_associations", curie=ALLIANCE.curie('phenotype_associations'),
                   model_uri=ALLIANCE.phenotype_associations, domain=None, range=Optional[Union[dict, PhenotypeAssociation]])

slots.disease_associations = Slot(uri=ALLIANCE.disease_associations, name="disease_associations", curie=ALLIANCE.curie('disease_associations'),
                   model_uri=ALLIANCE.disease_associations, domain=None, range=Optional[Union[dict, DiseaseAssociation]])
