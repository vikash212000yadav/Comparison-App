from django import forms


class FilterForm(forms.Form):

    def __init__(self, *args, **kwargs):
        # choices_company = kwargs.pop('choices_company')

        choices_chipset = kwargs.pop('choices_chipset')
        choices_benchmark = kwargs.pop('choices_benchmark')
        super(FilterForm, self).__init__(*args, **kwargs)

        # self.fields["Company"] = forms.MultipleChoiceField(choices=choices_company, widget=forms.CheckboxSelectMultiple(), required=True)

        # self.fields["Chipset"] = forms.MultipleChoiceField(choices=choices_chipset,
        #                                                   widget=forms.CheckboxSelectMultiple(), required=True)
        # self.fields["Benchmark"] = forms.MultipleChoiceField(choices=choices_benchmark,
        #                                                     widget=forms.CheckboxSelectMultiple(), required=True)

        self.fields["Chipset"] = forms.MultipleChoiceField(choices=choices_chipset,
                                                           widget=forms.SelectMultiple(), required=True)
        self.fields["Benchmark"] = forms.MultipleChoiceField(choices=choices_benchmark,
                                                             widget=forms.SelectMultiple(), required=True)
