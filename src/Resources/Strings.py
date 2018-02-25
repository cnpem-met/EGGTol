"""
# Module: Strings.py
# Descriptin: This module acts as a string resource. Other Python files can import all the
# strings in this module to further use.
"""

class MyStrings():
    """
    # Class: MyStrings
    # Description: This class contains strings for further use. Each string is stored as a
    class attribute, also known as a static attribute.
    """

    # Window Title Strings:
    applicationTitle = 'Point Cloud Generator'
    applicationVersion = 'v0.7.119'

    # MenuBar Strings:
    menuBarFile = 'File'
    menuBarPanels = 'Panels and menus'
    menuBarVisualization = 'Visualization'
    menuBarSelection = 'Selection methods'
    menuBarAbout = 'About this application'

    # Action Strings:

    # Pop-up Window Strings:
    popupExitTitle = 'Quit the ' + applicationTitle
    popupExitMessage = ('Are you sure you want to close the application?\n' +
                       'Unsaved changes will be lost.')
    popupExitButtonOK = 'Quit'
    popupExitButtonCancel = 'Cancel'

    popupCloseTitle = ''
    popupCloseMessage = ''
    popupCloseButtonOK = ''
    popupCloseButtonCancel = ''

    popupLoadingTitle = 'Computing...'

    popupInvalidNTitle = 'Invalid N Value'
    popupInvalidNDescription = ('The chosen N value is invalid.\n' +
                               'Use a numeric positive value written in N points/mm ' +
                               'or use a grid of N x N points.')

    popupInvalidPrecisionTitle = 'Invalid precision'
    popupInvalidPrecisionDescription = ('The chosen precision value is invalid.\n' +
                                        'Use a numeric positive precision between 10 ' +
                                        'and 50 and try again.')

    popupInvalidUVTitle = 'Invalid U and V values'
    popupInvalidUVDescription = ('The U and V values for the parametric discretization ' +
                                 'are invalids.\n' +
                                 'Use a numeric positive integer for both and try again.')

    popupOpenedIgesTitle = ''
    popupOpenedIgesDescription = ''

    # Specific Side Widget Strings:
    autoDiscretizeMenuDescription = ('The auto discretization method will discretize\n' +
                                     'all model faces with specified parameters.')
    autoDiscretizeApply = 'Apply auto discretization'

    defectsDescription = ('Select the desired transformation.<br><br>' +
                          'The translation and rotation operations can be applied<br>' +
                          'to a flat or curved surface.<br>')
    defectsOptionTranslation = 'Translation of a group of points'
    defectsOptionRotation = 'Rotation of a group of points'
    defectsOptionRandom = 'Generate random errors'

    discretizeDescription = ('Select a discretization option.<br><br>' +
                             'The auto discretization will work on all flat surfaces<br>' +
                             'of the CAD model following the desired precision<br>')
    discretizeOptionAuto = 'Automatic\nDiscretization'
    discretizeOptionFace = 'Flat Surface\nDiscretization'
    discretizeOptionCylinder = 'Cylindrical\nDiscretization'
    discretizeOptionConic = 'Conical\nDiscretization'
    discretizeOptionSphere = 'Spherical\nDiscretization'
    discretizeOptionSurface = 'Parametric\nDiscretization'

    faceDiscretizeMenuDescription = ('')

    translationDefectsDescription = ('')

    randomDefectsDescription = ('')

    # General Side Widget Strings:
    flatDiscretizationHeader = '<b><br>Discretization mode for flat surfaces:</b>'
    nonFlatDiscretizationHeader = '<b><br>Discretization mode for non-flat surfaces:</b>'
    selectionModeHeader = '<b>Selection mode</b>'

    gridDiscretization = 'N x N Grid Discretization'
    nonGridDiscretization = 'N points/mm Discretization'

    askingForNValue = 'Enter the value of N for discretization:'
    askingForPrecision = ('Enter the desired precision for cropping the\n' +
                         'points on curved boundary limits:')
    askingForUVDiscretization = ('Discretize non-flat surfaces using\n' +
                                 'UV Parametrization')
    askingForUParameter = 'U parameter value:'
    askingForVParameter = 'V parameter value:'
    askingForOffset = ''
    askingForXNormal = ''
    askingForYNormal = ''
    askingForZNormal = ''

    # MainWindow Properties Strings:
    currentSessionGeneratedPoints = 'Current Session Generated Points'

    # Welcome Menu Strings:
    welcomeMenuDescription = ('Welcome to the ' + applicationTitle + '!\n' +
                              'Version ' + applicationVersion + ' alpha release.\n\n' +
                              'Basic Functionality\n' +
                              '----------------------\n\n' +
                              '* To get started, make an .IGES file import using the IMPORT side widget.\n\n' +
                              '* To discretize a model, use the GENERATE CLOUD side widget.\n\n' +
                              '* To apply translational and rotational erros, use the GENERATE ERRORS side widget\n\n' +
                              '* To export the generated point cloud to a .pcd (Point Cloud Data) file or to a plain ' +
                              'text file (.txt), use the EXPORT menu.\n\n' +
                              '* To show the current entities of the opened file, use the ENTITIES menu.\n\n' +
                              'Important Notes\n' +
                              '--------------------\n\n' +
                              'The ' + applicationTitle + ' works only for CAD models represented by the 186th IGES ' +
                              'entity (Manifold Solid). IGES files specified by other entities will not be read by the ' +
                              'application.\n\n' +
                              'GitHub.com project\n' +
                              '-----------------------\n\n' +
                              'The full source code can be found through the github.com/hideak/pointCloudGenerator link.\n\n' +
                              'The source code is under the GNU free software license, and can be modifyed and distributed.')
