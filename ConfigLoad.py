import ConfigParser

class config_load:

    config_name="API_Config.ini"
    Config = ConfigParser.ConfigParser()
    Config.read(config_name)

    def ConfigSectionMap(self, section):
        _dict = {}
        options = self.Config.options(section)
        for option in options:
            try:
                _dict[option] = self.Config.get(section, option)
                if _dict[option] == -1:
                    print("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                _dict[option] = None
        return _dict


    def _parse(self):
        return_dict = {}
        return_dict['account_sid'] = self.ConfigSectionMap("API_options")['account_sid']
        return_dict['auth_token'] = self.ConfigSectionMap("API_options")['auth_token']
        return_dict['phone_number_source'] = self.ConfigSectionMap("API_options")['phone_number_source']
        return_dict['phone_number_target'] = self.ConfigSectionMap("Config Options")['phone_number_target']
        return_dict['subreddit_name'] = self.ConfigSectionMap("Config Options")['subreddit_name']
        return_dict['sort_by'] = self.ConfigSectionMap("Config Options")['sort_by']
        return_dict['upvotes_per_min_trigger'] = self.ConfigSectionMap("Config Options")['upvotes_per_min_trigger']
        return_dict['refresh_every'] = self.ConfigSectionMap("Config Options")['refresh_every']
        print "Loaded config options: \n"
        for key in return_dict:
            print("\t %s : %s" % (key, return_dict[key]))
        return return_dict
