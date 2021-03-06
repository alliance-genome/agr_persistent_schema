# Auto generated from allele.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-05-19 13:22
# Schema: Alliance-Schema-Prototype-Allele
#
# id: https://github.com/alliance-genome/agr_persistent_schema/src/schema/allele
# description:
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
from . affectedGenomicModel import AffectedGenomicModelId
from . core import GeneId
from . reference import ReferenceId
from linkml.utils.metamodelcore import Bool
from linkml_model.types import Boolean, Integer, String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
NLMID = CurieNamespace('NLMID', 'https://www.ncbi.nlm.nih.gov/nlmcatalog/?term=')
ALLIANCE = CurieNamespace('alliance', 'http://alliancegenome.org')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
FALDO = CurieNamespace('faldo', 'http://biohackathon.org/resource/faldo#')
GFF = CurieNamespace('gff', 'https://w3id.org/gff')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = CurieNamespace('', 'https://github.com/alliance-genome/agr_persistent_schema/src/schema/allele/')


# Types

# Class references



@dataclass
class Allele(YAMLRoot):
    """
    One of multiple possible forms of a functional genomic element (most often described as a locus or gene),
    differing from the reference DNA sequence. The genomic element can be endogenous or constructed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/allele/Allele")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Allele"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/allele/Allele")

    name: Optional[str] = None
    symbol: Optional[str] = None
    taxon_id: Optional[int] = None
    cross_references: Optional[Union[str, List[str]]] = empty_list()
    synonyms: Optional[Union[str, List[str]]] = empty_list()
    affected_genes: Optional[Union[Union[str, GeneId], List[Union[str, GeneId]]]] = empty_list()
    contains_construct: Optional[Union[dict, "Construct"]] = None
    molecular_mutation: Optional[str] = None
    functional_impact: Optional[str] = None
    generation_method: Optional[str] = None
    associated_references: Optional[Union[Union[dict, "ReferenceType"], List[Union[dict, "ReferenceType"]]]] = empty_list()
    associated_notes: Optional[Union[dict, "NoteType"]] = None
    germline_transmission_status: Optional[str] = None
    parent_cell_line: Optional[Union[dict, "CellLine"]] = None
    mutant_cell_lines: Optional[Union[Union[dict, "CellLine"], List[Union[dict, "CellLine"]]]] = empty_list()
    embryonic_stem_cell_lines: Optional[str] = None
    images: Optional[Union[dict, "Image"]] = None
    feature_type: Optional[str] = None
    origins: Optional[Union[Union[str, AffectedGenomicModelId], List[Union[str, AffectedGenomicModelId]]]] = empty_list()
    database_status: Optional[Union[str, "DatabaseStatuses"]] = None
    inheritence_mode: Optional[Union[str, "ModesOfInheritence"]] = None
    in_collection: Optional[str] = None
    transposon_insertion: Optional[str] = None
    aberration: Optional[str] = None
    is_extinct: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.symbol is not None and not isinstance(self.symbol, str):
            self.symbol = str(self.symbol)

        if self.taxon_id is not None and not isinstance(self.taxon_id, int):
            self.taxon_id = int(self.taxon_id)

        if self.cross_references is None:
            self.cross_references = []
        if not isinstance(self.cross_references, list):
            self.cross_references = [self.cross_references]
        self.cross_references = [v if isinstance(v, str) else str(v) for v in self.cross_references]

        if self.synonyms is None:
            self.synonyms = []
        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms]
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        if self.affected_genes is None:
            self.affected_genes = []
        if not isinstance(self.affected_genes, list):
            self.affected_genes = [self.affected_genes]
        self.affected_genes = [v if isinstance(v, GeneId) else GeneId(v) for v in self.affected_genes]

        if self.contains_construct is not None and not isinstance(self.contains_construct, Construct):
            self.contains_construct = Construct()

        if self.molecular_mutation is not None and not isinstance(self.molecular_mutation, str):
            self.molecular_mutation = str(self.molecular_mutation)

        if self.functional_impact is not None and not isinstance(self.functional_impact, str):
            self.functional_impact = str(self.functional_impact)

        if self.generation_method is not None and not isinstance(self.generation_method, str):
            self.generation_method = str(self.generation_method)

        if self.associated_references is None:
            self.associated_references = []
        if not isinstance(self.associated_references, list):
            self.associated_references = [self.associated_references]
        self.associated_references = [v if isinstance(v, ReferenceType) else ReferenceType(**v) for v in self.associated_references]

        if self.associated_notes is not None and not isinstance(self.associated_notes, NoteType):
            self.associated_notes = NoteType(**self.associated_notes)

        if self.germline_transmission_status is not None and not isinstance(self.germline_transmission_status, str):
            self.germline_transmission_status = str(self.germline_transmission_status)

        if self.parent_cell_line is not None and not isinstance(self.parent_cell_line, CellLine):
            self.parent_cell_line = CellLine()

        if self.mutant_cell_lines is None:
            self.mutant_cell_lines = []
        if not isinstance(self.mutant_cell_lines, list):
            self.mutant_cell_lines = [self.mutant_cell_lines]
        self.mutant_cell_lines = [v if isinstance(v, CellLine) else CellLine(**v) for v in self.mutant_cell_lines]

        if self.embryonic_stem_cell_lines is not None and not isinstance(self.embryonic_stem_cell_lines, str):
            self.embryonic_stem_cell_lines = str(self.embryonic_stem_cell_lines)

        if self.images is not None and not isinstance(self.images, Image):
            self.images = Image()

        if self.feature_type is not None and not isinstance(self.feature_type, str):
            self.feature_type = str(self.feature_type)

        if self.origins is None:
            self.origins = []
        if not isinstance(self.origins, list):
            self.origins = [self.origins]
        self.origins = [v if isinstance(v, AffectedGenomicModelId) else AffectedGenomicModelId(v) for v in self.origins]

        if self.database_status is not None and not isinstance(self.database_status, DatabaseStatuses):
            self.database_status = DatabaseStatuses(self.database_status)

        if self.inheritence_mode is not None and not isinstance(self.inheritence_mode, ModesOfInheritence):
            self.inheritence_mode = ModesOfInheritence(self.inheritence_mode)

        if self.in_collection is not None and not isinstance(self.in_collection, str):
            self.in_collection = str(self.in_collection)

        if self.transposon_insertion is not None and not isinstance(self.transposon_insertion, str):
            self.transposon_insertion = str(self.transposon_insertion)

        if self.aberration is not None and not isinstance(self.aberration, str):
            self.aberration = str(self.aberration)

        if self.is_extinct is not None and not isinstance(self.is_extinct, Bool):
            self.is_extinct = Bool(self.is_extinct)

        super().__post_init__(**kwargs)


@dataclass
class ReferenceType(YAMLRoot):
    """
    Describes the relation between a reference and an object
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/allele/ReferenceType")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ReferenceType"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/allele/ReferenceType")

    reference_association: Optional[Union[str, "ReferenceAssociationTypes"]] = None
    references: Optional[Union[Union[str, ReferenceId], List[Union[str, ReferenceId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.reference_association is not None and not isinstance(self.reference_association, ReferenceAssociationTypes):
            self.reference_association = ReferenceAssociationTypes(self.reference_association)

        if self.references is None:
            self.references = []
        if not isinstance(self.references, list):
            self.references = [self.references]
        self.references = [v if isinstance(v, ReferenceId) else ReferenceId(v) for v in self.references]

        super().__post_init__(**kwargs)


@dataclass
class NoteType(YAMLRoot):
    """
    Describes the relation between a note and an object
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/allele/NoteType")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "NoteType"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/allele/NoteType")

    note_association: Optional[Union[str, "NoteAssociationTypes"]] = None
    notes: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.note_association is not None and not isinstance(self.note_association, NoteAssociationTypes):
            self.note_association = NoteAssociationTypes(self.note_association)

        if self.notes is None:
            self.notes = []
        if not isinstance(self.notes, list):
            self.notes = [self.notes]
        self.notes = [v if isinstance(v, str) else str(v) for v in self.notes]

        super().__post_init__(**kwargs)


class Construct(YAMLRoot):
    """
    Dummy construct class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/allele/Construct")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Construct"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/allele/Construct")


class CellLine(YAMLRoot):
    """
    Dummy cell line class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/allele/CellLine")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CellLine"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/allele/CellLine")


class Image(YAMLRoot):
    """
    Dummy image class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/allele/Image")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Image"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/allele/Image")


class SequenceTargetingReagent(YAMLRoot):
    """
    Dummy sequence targeting reagent class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/allele/SequenceTargetingReagent")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SequenceTargetingReagent"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/allele/SequenceTargetingReagent")


# Enumerations
class DatabaseStatuses(EnumDefinitionImpl):

    live = PermissibleValue(text="live")
    dead = PermissibleValue(text="dead")
    suppressed = PermissibleValue(text="suppressed")
    history = PermissibleValue(text="history")
    private = PermissibleValue(text="private")
    approved = PermissibleValue(text="approved")

    _defn = EnumDefinition(
        name="DatabaseStatuses",
    )

class ReferenceAssociationTypes(EnumDefinitionImpl):

    molecular = PermissibleValue(text="molecular")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="ReferenceAssociationTypes",
    )

class NoteAssociationTypes(EnumDefinitionImpl):

    molecular = PermissibleValue(text="molecular")
    origin = PermissibleValue(text="origin")
    cytology = PermissibleValue(text="cytology")
    private = PermissibleValue(text="private")
    curator_comments = PermissibleValue(text="curator_comments")

    _defn = EnumDefinition(
        name="NoteAssociationTypes",
    )

class ModesOfInheritence(EnumDefinitionImpl):

    dominant = PermissibleValue(text="dominant")
    recessive = PermissibleValue(text="recessive")
    semi_dominant = PermissibleValue(text="semi_dominant")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="ModesOfInheritence",
    )

# Slots
class slots:
    pass

slots.affected_genes = Slot(uri=DEFAULT_.affected_genes, name="affected_genes", curie=DEFAULT_.curie('affected_genes'),
                   model_uri=DEFAULT_.affected_genes, domain=Allele, range=Optional[Union[Union[str, GeneId], List[Union[str, GeneId]]]])

slots.contains_construct = Slot(uri=DEFAULT_.contains_construct, name="contains_construct", curie=DEFAULT_.curie('contains_construct'),
                   model_uri=DEFAULT_.contains_construct, domain=Allele, range=Optional[Union[dict, "Construct"]])

slots.molecular_mutation = Slot(uri=DEFAULT_.molecular_mutation, name="molecular_mutation", curie=DEFAULT_.curie('molecular_mutation'),
                   model_uri=DEFAULT_.molecular_mutation, domain=Allele, range=Optional[str])

slots.functional_impact = Slot(uri=DEFAULT_.functional_impact, name="functional_impact", curie=DEFAULT_.curie('functional_impact'),
                   model_uri=DEFAULT_.functional_impact, domain=Allele, range=Optional[str])

slots.generation_method = Slot(uri=DEFAULT_.generation_method, name="generation_method", curie=DEFAULT_.curie('generation_method'),
                   model_uri=DEFAULT_.generation_method, domain=Allele, range=Optional[str])

slots.associated_references = Slot(uri=DEFAULT_.associated_references, name="associated_references", curie=DEFAULT_.curie('associated_references'),
                   model_uri=DEFAULT_.associated_references, domain=None, range=Optional[Union[Union[dict, ReferenceType], List[Union[dict, ReferenceType]]]])

slots.reference_association = Slot(uri=DEFAULT_.reference_association, name="reference_association", curie=DEFAULT_.curie('reference_association'),
                   model_uri=DEFAULT_.reference_association, domain=ReferenceType, range=Optional[Union[str, "ReferenceAssociationTypes"]])

slots.reference = Slot(uri=DEFAULT_.reference, name="reference", curie=DEFAULT_.curie('reference'),
                   model_uri=DEFAULT_.reference, domain=ReferenceType, range=Optional[Union[str, ReferenceId]])

slots.associated_notes = Slot(uri=DEFAULT_.associated_notes, name="associated_notes", curie=DEFAULT_.curie('associated_notes'),
                   model_uri=DEFAULT_.associated_notes, domain=None, range=Optional[Union[dict, NoteType]])

slots.note_association = Slot(uri=DEFAULT_.note_association, name="note_association", curie=DEFAULT_.curie('note_association'),
                   model_uri=DEFAULT_.note_association, domain=NoteType, range=Optional[Union[str, "NoteAssociationTypes"]])

slots.feature_type = Slot(uri=DEFAULT_.feature_type, name="feature_type", curie=DEFAULT_.curie('feature_type'),
                   model_uri=DEFAULT_.feature_type, domain=Allele, range=Optional[str])

slots.origins = Slot(uri=DEFAULT_.origins, name="origins", curie=DEFAULT_.curie('origins'),
                   model_uri=DEFAULT_.origins, domain=Allele, range=Optional[Union[Union[str, AffectedGenomicModelId], List[Union[str, AffectedGenomicModelId]]]])

slots.germline_transmission_status = Slot(uri=DEFAULT_.germline_transmission_status, name="germline_transmission_status", curie=DEFAULT_.curie('germline_transmission_status'),
                   model_uri=DEFAULT_.germline_transmission_status, domain=Allele, range=Optional[str])

slots.parent_cell_line = Slot(uri=DEFAULT_.parent_cell_line, name="parent_cell_line", curie=DEFAULT_.curie('parent_cell_line'),
                   model_uri=DEFAULT_.parent_cell_line, domain=Allele, range=Optional[Union[dict, "CellLine"]])

slots.mutant_cell_lines = Slot(uri=DEFAULT_.mutant_cell_lines, name="mutant_cell_lines", curie=DEFAULT_.curie('mutant_cell_lines'),
                   model_uri=DEFAULT_.mutant_cell_lines, domain=Allele, range=Optional[Union[Union[dict, "CellLine"], List[Union[dict, "CellLine"]]]])

slots.embryonic_stem_cell_lines = Slot(uri=DEFAULT_.embryonic_stem_cell_lines, name="embryonic_stem_cell_lines", curie=DEFAULT_.curie('embryonic_stem_cell_lines'),
                   model_uri=DEFAULT_.embryonic_stem_cell_lines, domain=None, range=Optional[str])

slots.images = Slot(uri=DEFAULT_.images, name="images", curie=DEFAULT_.curie('images'),
                   model_uri=DEFAULT_.images, domain=None, range=Optional[Union[dict, Image]])

slots.database_status = Slot(uri=DEFAULT_.database_status, name="database_status", curie=DEFAULT_.curie('database_status'),
                   model_uri=DEFAULT_.database_status, domain=None, range=Optional[Union[str, "DatabaseStatuses"]])

slots.inheritence_mode = Slot(uri=DEFAULT_.inheritence_mode, name="inheritence_mode", curie=DEFAULT_.curie('inheritence_mode'),
                   model_uri=DEFAULT_.inheritence_mode, domain=Allele, range=Optional[Union[str, "ModesOfInheritence"]])

slots.in_collection = Slot(uri=DEFAULT_.in_collection, name="in_collection", curie=DEFAULT_.curie('in_collection'),
                   model_uri=DEFAULT_.in_collection, domain=Allele, range=Optional[str])

slots.transposon_insertion = Slot(uri=DEFAULT_.transposon_insertion, name="transposon_insertion", curie=DEFAULT_.curie('transposon_insertion'),
                   model_uri=DEFAULT_.transposon_insertion, domain=Allele, range=Optional[str])

slots.aberration = Slot(uri=DEFAULT_.aberration, name="aberration", curie=DEFAULT_.curie('aberration'),
                   model_uri=DEFAULT_.aberration, domain=Allele, range=Optional[str])

slots.is_extinct = Slot(uri=DEFAULT_.is_extinct, name="is_extinct", curie=DEFAULT_.curie('is_extinct'),
                   model_uri=DEFAULT_.is_extinct, domain=Allele, range=Optional[Union[bool, Bool]])

slots.Allele_synonyms = Slot(uri=DEFAULT_.synonyms, name="Allele_synonyms", curie=DEFAULT_.curie('synonyms'),
                   model_uri=DEFAULT_.Allele_synonyms, domain=Allele, range=Optional[Union[str, List[str]]])
