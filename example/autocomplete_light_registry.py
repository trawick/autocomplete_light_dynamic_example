import autocomplete_light


class AutocompleteName(autocomplete_light.AutocompleteBase):

    def choices_for_request(self):
        partial_name = self.request.GET.get('q')
        return [
            name for name in ['Jeff', 'John', 'Jane']
            if name[:len(partial_name)].lower() == partial_name.lower()
        ]

autocomplete_light.register(AutocompleteName)
