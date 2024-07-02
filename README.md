Content - Dexterity Item
========================

For all vocabulary types we check three things

* searching - entering a term should show values that match the term
* available - if I've selected Term2, Term2 should not show again in the drop down.
* ordering - select2 lets you order the values by drag/drop. The request parameters must be passed accordingly
* context value - when the edit page is rendered, an existing value should be appropriately represented

SimpleVocabulary (no vocabulary factory)
----------------------------------------

singular - SelectFieldWidget

* searching - no issue
* available - n/a
* ordering - n/a
* context value - no issue

singular - AjaxSelectFieldWidget

* searching - shows all values, regardless of match
* available - n/a
* ordering - n/a
* context value - shows term value, not title

multiple - SelectFieldWidget

* searching - no issue
* available - no issue
* ordering - does not work
* context value - no issue

multiple - AjaxSelectFieldWidget

* searching - does not work; shows all values
* available - works
* ordering - no issues
* context value - shows term value, not title

IVocabularyFactory - function
-----------------------------

singular - SelectFieldWidget

* searching - works
* available - n/a
* ordering - n/a
* context value - no issues

singular - AjaxSelectFieldWidget

* searching - does not work; shows all values
* available - n/a
* ordering - n/a
* context value - no issues

multiple - SelectFieldWidget

* searching - works
* available - Sometimes this would work, sometimes it would display an existing value again as an option. Could not consistently reproduce.
* ordering - does not work
* context value - works

multiple - AjaxSelectFieldWidget

* searching - does not work; shows all values
* available - same as above
* ordering - works
* context value - works


IVocabularyFactory - class
--------------------------

singular - SelectFieldWidget

* searching - works
* available - n/a
* ordering - n/a
* context value - 

singular - AjaxSelectFieldWidget

* searching - works
* available - n/a
* ordering - n/a
* context value - works

multiple - SelectFieldWidget

* searching - works
* available - works
* ordering - does not work
* context value - works

multiple - AjaxSelectFieldWidget

* searching - works
* available - works
* ordering - works
* context value - works



StaticCatalogVocabulary
-----------------------

This is a named vocabulary from Plone that is meant to be used with Relation fields.

single - SelectFieldWidget

* searching - works
* available - n/a
* ordering - n/a
* context value - works

single - AjaxSelectFieldWidget

* searching - works
* available - works
* ordering - works
* context value - shows UID on edit page, not title

multiple - SelectFieldWidget

* searching - works
* available - works
* ordering - does not work
* context value - works

multiple - AjaxSelectFieldWidget

* searching - works
* available - works
* ordering - works
* context value - shows UID on edit page, not title
