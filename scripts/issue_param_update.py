class ParameterizedStorm(param.Parameterized):

    measured_parameter = param.ObjectSelector(
        objects=measured_parameter_options,
        default="turbidity",
        label="Measured parameter",
        doc="The parameter measured in-situ in the stream.",
    )
    locations_selected_on_map = param.ListSelector(
        label="Locations for cross-site comparison",
        doc="The locations to view and compare.",
    )
    single_location = param.ObjectSelector(
        label="Location for time-series plot",
        doc="A single location to plot time-series data from.",
    )
    # placeholder
    no_storm_selected_dict = {
        "Select a location!": 0,
        "Select any location!": 1,
    }
    single_storm_number = param.ObjectSelector(
        label="Storm for time-series plot",
        doc="A single storm to plot time-series data from.",
        objects=no_storm_selected_dict,
        default=0,
    )


    def __init__(self):
        super().__init__()
        # other stuff not related to the date parameter happens

    def get_discrete_storm_opts(
        self, the_param: str, the_location: str
    ) -> Tuple[Dict, int]:
        pk_data = self.by_storm_summary.loc[
            (self.by_storm_summary["measured_param"] == the_param)
            & (self.by_storm_summary["Location"] == the_location)
        ].reset_index()
        df2 = (
            pk_data[["date_text", "storm_number"]]
            .drop_duplicates()
            .set_index("date_text")
        )
        date_opts_dict = df2.to_dict()["storm_number"]
        if len(df2.index) > 0:
            init_selected_date = df2.index[0]
            return date_opts_dict, init_selected_date
        else:
            error_dict = {
                "No storms recorded for this param and location": 0,
                "Pick another location": 1,
            }
            return (
                error_dict,
                next(iter(error_dict)),
            )

    # This updates the date list available on the date slider based on the selected location
    @param.depends("single_location", watch=True)
    def _update_dates(self):
        print(
            strftime("%H:%M:%S  ", gmtime())
            + "_update_dates: Updating the possible storm dates based on {} at {}".format(
                self.measured_parameter, self.single_location
            )
        )
        one_loc = self.single_location
        cur_selected_storm_no = self.single_storm_number

        # If there is a single location selected, we get the possible storms
        # based on that location and the current parameter value
        if one_loc is not None:
            # given the current location and parameter, find the possible dates
            new_date_opts, new_selected_date = self.get_discrete_storm_opts(
                self.measured_parameter, self.single_location
            )
            # set the options to the full list of dates
            self.param["single_storm_number"].objects = new_date_opts
            new_selected_storm_no = new_selected_date
        # if there is not a single location selected
        else:
            # put in dummy values asking for a location to be selected
            self.param["single_storm_number"].objects = no_storm_selected_dict
            new_selected_storm_no = next(iter(no_storm_selected_dict))

        # if the value isn't changed (ie, 0 to 0) no trigger will happen for the
        # single_storm_number event, so we manually trigger it
        self.single_storm_number = new_selected_storm_no
        if new_selected_storm_no == cur_selected_storm_no:
            print(
                strftime("%H:%M:%S  ", gmtime())
                + "Manually triggering a single_storm_number event"
            )
            self.param.trigger("single_storm_number")
        print(strftime("%H:%M:%S  ", gmtime()) + "finished _update_dates")