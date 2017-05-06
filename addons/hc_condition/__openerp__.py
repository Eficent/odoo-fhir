# -*- coding: utf-8 -*-
{
    'name': "Condition",

    'summary': """
        Health states, problems or diagnoses
    """,

    # 'old description': """
    #     Detailed information about conditions, problems or diagnoses recognized by a clinician. 
    #     There are many uses including: recording a diagnosis during an encounter; 
    #     populating a problem list or a summary statement, such as a discharge summary.

    #     **Scope and Usage**

    #     Used to record detailed information pertinent to a clinician's assessment and assertion 
    #     of a particular aspect of a person's state of health. Examples of condition include problems, 
    #     diagnoses, concerns, issues. There are many uses of condition which include:
        
    #     * recording a problem, diagnosis, health concern or health issue during an encounter
    #     * the use of such information to populate a problem list of a summary statement such as a discharge summary
        
    #     This resource is used to record detailed information about a clinician's assessment and assertion 
    #     of a particular aspect of a patient's state of health. It is intended for use to record information 
    #     about a disease/illness identified from application of clinical reasoning over the pathologic 
    #     and pathophysiologic findings (diagnosis), or identification of health issues/situations that 
    #     require ongoing monitoring and/or management (health issue/concern), or identification of 
    #     health issues/situations considered harmful, potentially harmful and required to be investigated 
    #     and managed (problems).

    #     The condition resource may also be used to record certain health state of a patient 
    #     which does not normally present negative outcome (until complications are predicted or detected), 
    #     e.g. pregnancy. Examples of complications of pregnancy include: hyperemesis gravidarum, 
    #     preeclampsia, eclampsia - which are captured as problems/diagnoses.
    #     """,

        'description': """

        A clinical condition, problem, diagnosis, or other event, situation, issue, or clinical concept that has risen to a level of concern. 
        
        **Scope and Usage**

        Condition is one of the event resources in the FHIR workflow specification.

        This resource is used to record detailed information about a condition, problem, diagnosis, or other event, situation, issue, or clinical concept 
        that has risen to a level of concern. The condition could be a point in time diagnosis in context of an encounter, it could be an item on the practitioner’s 
        Problem List, or it could be a concern that doesn’t exist on the practitioner’s Problem List. Often times, a condition is about a clinician's assessment 
        and assertion of a particular aspect of a patient's state of health. It can be used to record information about a disease/illness identified from application 
        of clinical reasoning over the pathologic and pathophysiologic findings (diagnosis), or identification of health issues/situations that a practitioner considers 
        harmful, potentially harmful and may be investigated and managed (problem), or other health issue/situation that may require ongoing monitoring and/or management 
        (health issue/concern). 
        
        The condition resource may be used to record a certain health state of a patient which does not normally present a negative outcome, e.g. pregnancy. 
        The condition resource may be used to record a condition following a procedure, such as the condition of Amputee-BKA following an amputation procedure. 
        
        While conditions are frequently a result of a clinician's assessment and assertion of a particular aspect of a patient's state of health, 
        conditions can also be expressed by the patient, related person, or any care team member. A clinician may have a concern about a patient condition (e.g. anorexia) 
        that the patient is not concerned about. Likewise, the patient may have a condition (e.g. hair loss) that does not rise to the level of importance 
        such that it belongs on a practitioner’s Problem List. 
        
        For example, each of the following conditions could rise to the level of importance such that it belongs on a problem or concern list due to its 
        direct or indirect impact on the patient’s health. These examples may also be represented using other resources, such as FamilyMemberHistory, Observation, or Procedure. 
        
        * Unemployed
        * Without transportation (or other barriers)
        * Susceptibility to falls
        * Exposure to communicable disease
        * Family History of cardiovascular disease
        * Fear of cancer
        * Cardiac pacemaker
        * Amputee-BKA
        * Risk of Zika virus following travel to a country 
        * Former smoker
        * Travel to a country planned (that warrants immunizations)
        * Motor Vehicle Accident
        * Patient has had coronary bypass graft
    """,

    'author': "FHIR® and Luigi Sison",
    'website': "https://hl7-fhir.github.io/condition.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_group'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_condition_views.xml',
        'views/hc_res_condition_templates.xml',
        # 'data/hc.vs.condition.category.csv',
        # 'data/hc.vs.condition.code.csv',
        # 'data/hc.vs.condition.evidence.code.csv',
        # 'data/hc.vs.condition.severity.csv',
        # 'data/hc.vs.condition.stage.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}