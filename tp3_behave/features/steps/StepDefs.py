from behave import *
import EventManager
import io
import sys

testManager = EventManager.EventManager()
capturedOutput = io.StringIO()


@given("John est sur le menu principal")
def step_impl(context):
    testManager.menu()


@when('John ajoute un nouveau rendez-vous avec le titre "Réunion client" à la date et heure spécifiées')
def step_impl(context):
    testManager.addEvent("Réunion client", "2020-01-01", "10:00")


@then("le rendez-vous est affiché dans la liste de rdvs")
def step_impl(context):
    assert "Réunion client, 2020-01-01, 10:00" in testManager.showEvents()


@given("John a plusieurs rendez-vous")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    testManager.addEvent("Réunion client", "2020-01-01", "10:00")
    testManager.addEvent("Réunion équipe", "2020-01-02", "11:00")
    testManager.addEvent("Réunion stratégique", "2020-01-03", "12:00")
    testManager.addEvent("Entretien d'embauche", "2020-01-04", "13:00")


@when("John consulte la liste")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    sys.stdout = capturedOutput
    events = testManager.showEvents()
    assert events == "Réunion client, 2020-01-01, 10:00\nRéunion équipe, 2020-01-02, 11:00\nRéunion stratégique, 2020-01-03, 12:00\nEntretien d'embauche, 2020-01-04, 13:00"


@then("la liste est affiché")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == "Réunion client, 2020-01-01, 10:00\nRéunion équipe, 2020-01-02, 11:00\nRéunion stratégique, 2020-01-03, 12:00\nEntretien d'embauche, 2020-01-04, 13:00\n"


@given("John a des rendez-vous")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    testManager.addEvent("Réunion client", "2020-01-01", "10:00")
    testManager.addEvent("Réunion équipe", "2020-01-02", "11:00")
    testManager.addEvent("Réunion stratégique", "2020-01-03", "12:00")
    testManager.addEvent("Entretien d'embauche", "2020-01-04", "13:00")


@when('John sélectionne le rendez-vous "Entretien d\'embauche" et le supprime')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    testManager.deleteEvent("Entretien d'embauche")


@then('le rendez-vous "Entretien d\'embauche" est retiré de la liste des rendez-vous')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert "Entretien d'embauche, 2020-01-04, 13:00" not in testManager.showEvents()


@given('John a créé un rendez-vous "Réunion d\'équipe" avec une description')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    testManager.addEvent("Réunion d'équipe", "2020-01-01", "10:00", "Réunion d'équipe")


@when('John modifie la description du rendez-vous en "Réunion stratégique"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    testManager.editEvent("Réunion d'équipe", "Réunion stratégique")


@then('le rendez-vous "Réunion d\'équipe" affiche maintenant la nouvelle description')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert "Réunion stratégique" in testManager.showEvents()


@given("John a deux rendez-vous programmés pour la même heure")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    testManager.addEvent("Réunion client", "2020-01-01", "10:00")
    testManager.addEvent("Réunion équipe", "2020-01-01", "10:00")


@when("John essaie d'ajouter un troisième rendez-vous en même temps")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    testManager.addEvent("Réunion stratégique", "2020-01-01", "10:00")


@then("le système affiche un message d'erreur indiquant un conflit d'horaire")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert "Conflit d'horaire" in testManager.showEvents()
