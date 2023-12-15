Feature: Gestion d'évènements

  En tant que John, je veux pouvoir gérer mes rendez-vous

  Scenario: Ajouter un rendez-vous
    Given John est sur le menu principal
    When John ajoute un nouveau rendez-vous avec le titre "Réunion client" à la date et heure spécifiées
    Then le rendez-vous est affiché dans la liste de rdvs

  Scenario: Afficher la liste des rendez-vous
    Given John a plusieurs rendez-vous
    When John consulte la liste
    Then la liste est affiché

  Scenario: Supprimer un rendez-vous
    Given John a des rendez-vous
    When John sélectionne le rendez-vous "Entretien d'embauche" et le supprime
    Then le rendez-vous "Entretien d'embauche" est retiré de la liste des rendez-vous

  Scenario: Modifier les détails d'un rendez-vous
    Given John a créé un rendez-vous "Réunion d'équipe" avec une description
    When John modifie la description du rendez-vous en "Réunion stratégique"
    Then le rendez-vous "Réunion d'équipe" affiche maintenant la nouvelle description

  Scenario: Gérer les conflits de rendez-vous
    Given John a deux rendez-vous programmés pour la même heure
    When John essaie d'ajouter un troisième rendez-vous en même temps
    Then le système affiche un message d'erreur indiquant un conflit d'horaire