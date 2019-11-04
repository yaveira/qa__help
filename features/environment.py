"""Hooks file."""

from behave.tag_matcher import ActiveTagMatcher
from behave.model import Scenario

active_tag_value_provider = {
    "config_0": False
}

active_tag_matcher = ActiveTagMatcher(active_tag_value_provider)


def before_all(context):
    global userdata

    userdata = context.config.userdata
    context.config_0 = userdata.get('config_0', 'False')
    continue_after_failed = userdata.getbool("runner.continue_after_failed_step", False)
    Scenario.continue_after_failed_step = continue_after_failed


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    if active_tag_matcher.should_exclude_with(scenario.effective_tags):
        scenario.skip(reason="DISABLED ACTIVE-TAG")


def before_tag(context, tag):
    if tag == 'token':
        from features.utils.gerar_token import GerarToken

        context.token = GerarToken.gerar_token(context, 'api/v1/token')


def after_step(context, step):
    pass


def after_tag(context, tag):
    pass


def after_scenario(context, scenario):
    pass


def after_feature(context, feature):
    pass


def after_all(context):
    pass
