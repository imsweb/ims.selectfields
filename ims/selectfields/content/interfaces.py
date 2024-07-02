import zope.schema as schema
from plone.app.z3cform.widgets.select import AjaxSelectFieldWidget
from plone.app.z3cform.widgets.select import SelectFieldWidget
from plone.autoform import directives
from plone.supermodel import model
from .vocabulary import static_vocabulary
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from plone.app.vocabularies.catalog import StaticCatalogVocabulary


class ISimpleVocabulary(model.Schema):
    """ """
    directives.widget('singular', SelectFieldWidget)
    singular = schema.Choice(
        title='SimpleVocbulary - singular - SelectFieldWidget',
        required=False,
        vocabulary=static_vocabulary,
    )
    directives.widget('singular_ajax', AjaxSelectFieldWidget)
    singular_ajax = schema.Choice(
        title='SimpleVocabulary - singular - AjaxSelectFieldWidget',
        required=False,
        vocabulary=static_vocabulary,
    )
    directives.widget('multiple', SelectFieldWidget)
    multiple = schema.List(
        title='SimpleVocabulary - multiple - SelectFieldWidget',
        required=False,
        value_type=schema.Choice(
            vocabulary=static_vocabulary,
        )
    )
    directives.widget('multiple_ajax', AjaxSelectFieldWidget)
    multiple_ajax = schema.List(
        title='SimpleVocabulary - multiple - AjaxSelectFieldWidget',
        required=False,
        value_type=schema.Choice(
            vocabulary=static_vocabulary,
        )
    )


class IVocabularyFactoryFunction(model.Schema):
    directives.widget('singular', SelectFieldWidget)
    singular = schema.Choice(
        title='IVocabularyFactory function - singular - SelectFieldWidget',
        required=False,
        vocabulary='ims.selectfields.vf_function',
    )
    directives.widget('singular_ajax', AjaxSelectFieldWidget)
    singular_ajax = schema.Choice(
        title='IVocabularyFactory function - singular - AjaxSelectFieldWidget',
        required=False,
        vocabulary='ims.selectfields.vf_function',
    )
    directives.widget('multiple', SelectFieldWidget)
    multiple = schema.List(
        title='IVocabularyFactory function - multiple - SelectFieldWidget',
        required=False,
        value_type=schema.Choice(
            vocabulary='ims.selectfields.vf_function',
        )
    )
    directives.widget('multiple_ajax', AjaxSelectFieldWidget)
    multiple_ajax = schema.List(
        title='IVocabularyFactory function - multiple - AjaxSelectFieldWidget',
        required=False,
        value_type=schema.Choice(
            vocabulary='ims.selectfields.vf_function',
        )
    )


class IVocabularyFactoryClass(model.Schema):
    directives.widget('singular', SelectFieldWidget)
    singular = schema.Choice(
        title='IVocabularyFactory class - singular - SelectFieldWidget',
        required=False,
        vocabulary='ims.selectfields.vf_class',
    )
    directives.widget('singular_ajax', AjaxSelectFieldWidget)
    singular_ajax = schema.Choice(
        title='IVocabularyFactory class - singular - AjaxSelectFieldWidget',
        required=False,
        vocabulary='ims.selectfields.vf_class',
    )
    directives.widget('multiple', SelectFieldWidget)
    multiple = schema.List(
        title='IVocabularyFactory class - multiple - SelectFieldWidget',
        required=False,
        value_type=schema.Choice(
            vocabulary='ims.selectfields.vf_class',
        )
    )
    directives.widget('multiple_ajax', AjaxSelectFieldWidget)
    multiple_ajax = schema.List(
        title='IVocabularyFactory class - multiple - AjaxSelectFieldWidget',
        required=False,
        value_type=schema.Choice(
            vocabulary='ims.selectfields.vf_class',
        )
    )


class IRelationClass(model.Schema):
    directives.widget('singular', SelectFieldWidget)
    singular = RelationChoice(
        title='StaticCatalogVocabulary - singular - SelectFieldWidget',
        required=False,
        vocabulary=StaticCatalogVocabulary(
            {
                "object_provides": "plone.app.contenttypes.interfaces.IDocument",
            },
            title_template="{brain.Title}"
        ),
    )
    directives.widget('singular_ajax', AjaxSelectFieldWidget)
    singular_ajax = RelationChoice(
        title='StaticCatalogVocabulary - singular - AjaxSelectFieldWidget',
        required=False,
        vocabulary=StaticCatalogVocabulary(
            {
                "object_provides": "plone.app.contenttypes.interfaces.IDocument",
            },
            title_template="{brain.Title}"
        ),
    )
    directives.widget('multiple', SelectFieldWidget)
    multiple = RelationList(
        title='StaticCatalogVocabulary - multiple - SelectFieldWidget',
        required=False,
        value_type=RelationChoice(
            vocabulary=StaticCatalogVocabulary(
                {
                    "object_provides": "plone.app.contenttypes.interfaces.IDocument",
                },
                title_template="{brain.Title}"
            )),
    )
    directives.widget('multiple_ajax', AjaxSelectFieldWidget)
    multiple_ajax = RelationList(
        title='StaticCatalogVocabulary - multiple - AjaxSelectFieldWidget',
        required=False,
        value_type=RelationChoice(
            vocabulary=StaticCatalogVocabulary(
                {
                    "object_provides": "plone.app.contenttypes.interfaces.IDocument",
                },
                title_template="{brain.Title}"
            )),
    )
