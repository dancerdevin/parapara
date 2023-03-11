from django.db import models

# ParaPara 1.0 is divided into three phases of model implementation: the Arc, Mission, and Quest phases.
# (1) The Arc phase includes the User, Character, Arc, Paradigm, Parameter, and EventLog models.
# This enables Users to create a Character and an Arc, define the Character's Paradigms and Parameters, and create
# EventLogs associated with an Arc. In sum: to make journal entries and earn XP for doing so.
# (2) The Mission phase includes Missions and MissionLog models.
# This enables Users to define Missions and their cadence (e.g., daily, weekly, non-recurring) and mark them complete.
# In sum: to earn XP without necessarily making journal entries, and instead by checking off possibly-regular tasks.
# (3) The Quest phase includes the Quest/QuestTree model, a planned meta-structure for Missions.
# This is intended to be a way to group Missions in relation to each other for improved organization and more XP gain.


# Arc Phase Models


class User(models.Model):
    # Users will have a username, password, Characters, and display name. (What other info might I want?)
    username = models.CharField(
        'Username',
        default='New User',
        max_length=30,
        blank=False,
        null=False
    )
    password = models.CharField(
        'User password',
        max_length=30,
        blank=False,
        null=False
    )
    characters = models.ForeignKey(
        'Character',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    display_name = models.CharField(
        'User display name',
        max_length=30,
        blank=True,
        null=True
    )
    email = models.CharField(
        'I guess I should ask for an email for password recovery or something',
        max_length=50,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username


class Character(models.Model):
    # Characters will have Arcs, Paradigms, and Parameters. (EventLogs will be grouped under Arcs.)
    # The purpose of the Character/Arc distinction is to allow a User to "start fresh" while optionally carrying
    # some or all of their Paradigm or Parameter data with them (or to make implementing that functionality easier).
    # And if a User wants to start completely from scratch without deleting any data, they can make a new Character.
    name = models.CharField(
        'Character name',
        default='New Character',
        max_length=30,
        blank=False,
        null=False
    )
    arcs = models.ForeignKey(
        'Arc',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    paradigms = models.ForeignKey(
        'Paradigm',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    parameters = models.ForeignKey(
        'Parameter',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

class Arc(models.Model):
    # Arcs will have EventLogs and a Description. Eventually: Missions, MissionLogs, and Quest/QuestTrees, too.
    # Arcs are like storylines, i.e., "narrative arcs." The same Character may have multiple Arcs. EventLogs are
    # then like chapters or paragraphs of a story, and so belong to an Arc. But the "stats," e.g., Paradigms and
    # Parameters, belong to the Character, not necessarily any particular Arc.
    name = models.CharField(
        'Arc name',
        default='New Arc',
        max_length=30,
        blank=False,
        null=False
    )
    event_logs = models.ForeignKey(
        'EventLog',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    description = models.CharField(
        'A brief, optional description of this Arc',
        max_length=100,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

class Paradigm(models.Model):
    # Paradigms will have a Name, Description, Default_Parameters (ForeignKey), Level, XP, Total_XP, and Next_Level_XP.
    # Paradigms are like character classes or alter egos; they represent different goals and emphasize different
    # qualities. They are thus associated with default Parameters, like Fighters with Strength and Clerics with Wisdom.
    name = models.CharField(
        'Paradigm name',
        default='New Paradigm',
        max_length=20,
        blank=False,
        null=False
    )
    description = models.CharField(
        'Brief, optional description of Paradigm',
        max_length=100,
        blank=True,
        null=True
    )
    default_parameters = models.ManyToManyField(
        'Parameter'
    )
    level = models.IntegerField(
        'Experience level of this Paradigm',
        default=1
    )
    xp = models.IntegerField(
        'Experience points gained for this Paradigm since last level up',
        default=0
    )
    total_xp = models.IntegerField(
        'Total experience points gained for this Paradigm',
        default=0
    )
    next_level_xp = models.IntegerField(
        'The number that XP (not total_XP) should be to reach the next level',
        default=50
    )

    def __str__(self):
        return self.name

class Parameter(models.Model):
    # Parameters will have a Name, Description, Level, XP, Total_XP, and Next_Level_XP.
    # Parameters are like stats or attributes; they represent distinct valued capacities, relevant to Paradigms.
    # The same Parameter may be relevant to, and so gain XP in concert with, multiple different Paradigms.
    name = models.CharField(
        'Parameter name',
        default='New Parameter',
        max_length=20,
        blank=False,
        null=False
    )
    description = models.CharField(
        'Brief, optional description of Parameter',
        max_length=100,
        blank=True,
        null=True
    )
    level = models.IntegerField(
        'Experience level of this Parameter',
        default=10
    )
    xp = models.IntegerField(
        'Experience points gained for this Parameter since last level up',
        default=0
    )
    total_xp = models.IntegerField(
        'Total experience points gained for this Parameter',
        default=0
    )
    next_level_xp = models.IntegerField(
        'The number that XP (not total_XP) should be to reach the next level',
        default=50
    )

    def __str__(self):
        return self.name

class EventLog(models.Model):
    # EventLogs will have an ID, Name, Date, Tagged_Paradigms, Tagged_Parameters, Significance_Mod, and Entry_Text.
    # The assumption of ParaPara is that every event represents some side of oneself, i.e., a Paradigm. Users are
    # expected to tag a Paradigm, which grants XP to that Paradigm and its Default_Parameters, when making an EventLog.
    # However, Users may directly tag Parameters as well or if they prefer (because why not?).
    # I shouldn't need to specify a model for event IDs because those will be automatically assigned as primary_key.
    name = models.CharField(
        'Event name',
        default='New Event',
        max_length=30,
        blank=True,
        null=True
    )
    event_date = models.DateTimeField(
        'Event date and time',
        blank=False,
        null=False
    )
    tagged_paradigms = models.ManyToManyField(
        'Paradigm',
        # Determines which Paradigms and default_parameters gain XP
        blank=True
    )
    tagged_parameters = models.ManyToManyField(
        'Parameter',
        # Determines which Parameters gain XP, additive on any XP from default_parameters of tagged Paradigms
        blank=True
    )
    significance_mod = models.IntegerField(
        'A modifier representing the significance of the event; functions as a XP multiplier',
        default=1
    )
    content = models.TextField(
        'The main content of the EventLog',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

