"""Compares a Panel app to a Mercury app"""
# pylint: skip-file
import panel as pn
from bloxs import B as _B


from awesome_panel import config

config.extension(url="mercury_buy_vs_build")


US_WORKING_DAYS_PER_YEAR = 261
LICENSE_COST = {
    "Free, open source": 0,
    "Single": 995,
    "Small Business": 995,
    "Enterprise": 9500,
}


def license_cost(license_type):
    return LICENSE_COST[license_type]


def cost_to_build(number_of_employees_required, average_employee_salary, days_to_build):
    return (
        number_of_employees_required
        * average_employee_salary
        * days_to_build
        / US_WORKING_DAYS_PER_YEAR
    )


def cost_to_maintain(average_employee_salary, days_per_month_for_maintenance):
    return days_per_month_for_maintenance * 12 * average_employee_salary / US_WORKING_DAYS_PER_YEAR


def saved_annually(
    number_of_employees_required,
    average_employee_salary,
    days_to_build,
    days_per_month_for_maintenance,
    license_type,
):
    cost_license = license_cost(license_type)
    cost_build = cost_to_build(number_of_employees_required, average_employee_salary, days_to_build)
    cost_maintenance = cost_to_maintain(average_employee_salary, days_per_month_for_maintenance)
    return cost_license - cost_build - cost_maintenance


pn.extension(sizing_mode="stretch_width")

settings_header = "# Buy 💸 vs build 🛠️"
license_type = pn.widgets.Select(
    value="Single", options=list(LICENSE_COST), name="Please select license"
)
number_of_employees_required = pn.widgets.IntSlider(
    value=2, start=1, end=5, name="Number of employees required"
)
average_employee_salary = pn.widgets.IntSlider(
    value=90000, start=10000, end=300000, step=10000, name="Average employee salary"
)
days_to_build = pn.widgets.IntSlider(value=5, start=1, end=30, name="Days to build")
days_per_month_for_maintenance = pn.widgets.IntSlider(
    value=1, start=0, end=5, name="Days per month for maintenance"
)


def B(
    *args, width="100%", height="150px", margin="0px", padding_top="40px", background="transparent", text_color="var(--neutral-foreground-rest)"
):
    """Returns a modified version of B that works better with Bokeh/ Panel"""
    return (
        _B(*args)
        ._repr_html_()
        .replace("width: 34%", f"width: {width}; height: {height}")
        .replace("margin: 10px; padding-top: 40px", f"margin: {margin}; padding-top: {padding_top}")
        .replace("background: white", f"background: {background}")
        .replace("color: #5a5a5a", f"color: {text_color}")
        .replace("color: gray", f"color: {text_color}")
    )


@pn.depends(license_type)
def license_type_blox(license):
    return B("📜", license)


@pn.depends(license_type)
def license_cost_blox(license_type):
    cost = license_cost(license_type)
    return B(f"${cost:,.0f}", "License Cost")


buy_vs_build_blox = B("💸 🛠️", "Buy vs build")


@pn.depends(number_of_employees_required, average_employee_salary, days_to_build)
def cost_to_build_blox(number_of_employees_required, average_employee_salary, days_to_build):
    cost = cost_to_build(number_of_employees_required, average_employee_salary, days_to_build)
    return B(f"${cost:,.0f}", "Cost to build")


@pn.depends(average_employee_salary, days_per_month_for_maintenance)
def cost_to_maintain_blox(average_employee_salary, days_per_month_for_maintenance):
    cost = cost_to_maintain(average_employee_salary, days_per_month_for_maintenance)
    return B(f"${cost:,.0f}", "Annual Maintenance")


@pn.depends(
    number_of_employees_required,
    average_employee_salary,
    days_to_build,
    days_per_month_for_maintenance,
    license_type,
)
def saved_annually_blox(
    number_of_employees_required,
    average_employee_salary,
    days_to_build,
    days_per_month_for_maintenance,
    license_type,
):
    saved = saved_annually(
        number_of_employees_required,
        average_employee_salary,
        days_to_build,
        days_per_month_for_maintenance,
        license_type,
    )
    return B(f"${saved:,.0f}", "Saved annually")


pn.Row(
    pn.Column(
        settings_header,
        license_type,
        number_of_employees_required,
        average_employee_salary,
        days_to_build,
        days_per_month_for_maintenance,
        sizing_mode="fixed",
        width=300,
    ),
    pn.Column(
        pn.Row(
            pn.panel(license_type_blox, height=300),
            license_cost_blox,
            buy_vs_build_blox,
            margin=(5, 10, -15, 10),
        ),
        pn.Row(
            cost_to_build_blox, cost_to_maintain_blox, saved_annually_blox, margin=(-15, 10, 5, 10)
        ),
    ),
).servable()
