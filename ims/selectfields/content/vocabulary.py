from zope.interface import provider
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

static_vocabulary = SimpleVocabulary([
    SimpleTerm(value='term1', title='Term1'),
    SimpleTerm(value='term2', title='Term2'),
    SimpleTerm(value='term3', title='Term3'),
])


@provider(IVocabularyFactory)
def vocabulary_factory(context):
    return SimpleVocabulary([
        SimpleTerm(value='term1', title='Term1'),
        SimpleTerm(value='term2', title='Term2'),
        SimpleTerm(value='term3', title='Term3'),
    ])


@implementer(IVocabularyFactory)
class Vocabulary(object):
    """ Differs from UniqueIndexVocabulary in that all_terms returns terms not items """

    def all_terms(self):
        return [
            SimpleTerm(value='orange', title='Orange'),
            SimpleTerm(value='banana', title='Banana'),
            SimpleTerm(value='cherry', title='Cherry'),
        ]

    def match_terms(self, query):
        if query:
            return sorted([term for term in self.all_terms() if query.lower() in term.value],
                          key=lambda term: term.title)
        else:
            return sorted(self.all_terms(), key=lambda term: term.title)

    def __call__(self, context, query=None):
        return SimpleVocabulary(self.match_terms(query))


VocabularyFactory = Vocabulary()
