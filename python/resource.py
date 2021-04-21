# Auto generated from resource.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-04-14 16:48
# Schema: resource
#
# id: https://github.com/alliance-genome/agr_persistent_schema/src/schema/resource
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
from . core import Id
from . informationContentEntity import AuthorReference, InformationContentEntity
from . reference import ReferenceId
from linkml.utils.metamodelcore import URIorCURIE, XSDDate
from linkml_model.types import Date, String, Uriorcurie

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DOI = CurieNamespace('DOI', 'http://identifiers.org/doi/')
FB = CurieNamespace('FB', 'http://identifiers.org/fb/')
MGI = CurieNamespace('MGI', 'http://identifiers.org/mgi/')
NLMID = CurieNamespace('NLMID', 'http://example.org/UNKNOWN/NLMID/')
PMID = CurieNamespace('PMID', 'http://www.ncbi.nlm.nih.gov/pubmed/')
RGD = CurieNamespace('RGD', 'http://identifiers.org/rgd/')
SGD = CurieNamespace('SGD', 'http://identifiers.org/sgd/')
WB = CurieNamespace('WB', 'http://identifiers.org/wb/')
ZFIN = CurieNamespace('ZFIN', 'http://identifiers.org/zfin/')
DEFAULT_ = CurieNamespace('', 'https://github.com/alliance-genome/agr_persistent_schema/src/schema/resource/')


# Types

# Class references
class ResourceId(URIorCURIE):
    pass


@dataclass
class Resource(InformationContentEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/resource/Resource")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "resource"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/resource/Resource")

    id: Union[str, ResourceId] = None
    title: Optional[str] = None
    iso_abbreviation: Optional[str] = None
    medline_abbreviation: Optional[str] = None
    copyright_date: Optional[Union[str, XSDDate]] = None
    print_issn: Optional[str] = None
    online_issn: Optional[str] = None
    publisher: Optional[Union[dict, InformationContentEntity]] = None
    volumes: Optional[str] = None
    summary: Optional[str] = None
    synonyms: Optional[str] = None
    references: Optional[Union[Union[str, ReferenceId], List[Union[str, ReferenceId]]]] = empty_list()
    authors: Optional[Union[Union[dict, AuthorReference], List[Union[dict, AuthorReference]]]] = empty_list()
    editors: Optional[Union[Union[dict, AuthorReference], List[Union[dict, AuthorReference]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ResourceId):
            self.id = ResourceId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.iso_abbreviation is not None and not isinstance(self.iso_abbreviation, str):
            self.iso_abbreviation = str(self.iso_abbreviation)

        if self.medline_abbreviation is not None and not isinstance(self.medline_abbreviation, str):
            self.medline_abbreviation = str(self.medline_abbreviation)

        if self.copyright_date is not None and not isinstance(self.copyright_date, XSDDate):
            self.copyright_date = XSDDate(self.copyright_date)

        if self.print_issn is not None and not isinstance(self.print_issn, str):
            self.print_issn = str(self.print_issn)

        if self.online_issn is not None and not isinstance(self.online_issn, str):
            self.online_issn = str(self.online_issn)

        if self.publisher is not None and not isinstance(self.publisher, InformationContentEntity):
            self.publisher = InformationContentEntity(**self.publisher)

        if self.volumes is not None and not isinstance(self.volumes, str):
            self.volumes = str(self.volumes)

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        if self.synonyms is not None and not isinstance(self.synonyms, str):
            self.synonyms = str(self.synonyms)

        if self.references is None:
            self.references = []
        if not isinstance(self.references, list):
            self.references = [self.references]
        self.references = [v if isinstance(v, ReferenceId) else ReferenceId(v) for v in self.references]

        if self.authors is None:
            self.authors = []
        if not isinstance(self.authors, list):
            self.authors = [self.authors]
        self.authors = [v if isinstance(v, AuthorReference) else AuthorReference(**v) for v in self.authors]

        if self.editors is None:
            self.editors = []
        if not isinstance(self.editors, list):
            self.editors = [self.editors]
        self.editors = [v if isinstance(v, AuthorReference) else AuthorReference(**v) for v in self.editors]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.iso_abbreviation = Slot(uri=DEFAULT_.iso_abbreviation, name="iso abbreviation", curie=DEFAULT_.curie('iso_abbreviation'),
                   model_uri=DEFAULT_.iso_abbreviation, domain=Resource, range=Optional[str])

slots.medline_abbreviation = Slot(uri=DEFAULT_.medline_abbreviation, name="medline abbreviation", curie=DEFAULT_.curie('medline_abbreviation'),
                   model_uri=DEFAULT_.medline_abbreviation, domain=Resource, range=Optional[str])

slots.print_issn = Slot(uri=DEFAULT_.print_issn, name="print issn", curie=DEFAULT_.curie('print_issn'),
                   model_uri=DEFAULT_.print_issn, domain=Resource, range=Optional[str])

slots.online_issn = Slot(uri=DEFAULT_.online_issn, name="online issn", curie=DEFAULT_.curie('online_issn'),
                   model_uri=DEFAULT_.online_issn, domain=Resource, range=Optional[str])

slots.editors = Slot(uri=DEFAULT_.editors, name="editors", curie=DEFAULT_.curie('editors'),
                   model_uri=DEFAULT_.editors, domain=Resource, range=Optional[Union[Union[dict, AuthorReference], List[Union[dict, AuthorReference]]]])

slots.resource_id = Slot(uri=DEFAULT_.id, name="resource_id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.resource_id, domain=Resource, range=Union[str, ResourceId])

slots.resource_title = Slot(uri=DEFAULT_.title, name="resource_title", curie=DEFAULT_.curie('title'),
                   model_uri=DEFAULT_.resource_title, domain=Resource, range=Optional[str])