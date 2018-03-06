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
    applicationVersion = 'v0.7.134'

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

    popupOpenedIgesTitle = 'IGES File is already opened'
    popupOpenedIgesDescription1 = 'The file '
    popupOpenedIgesDescription2 = (' is already opened. Finish your activities and close the current ' +
                                   'file to import a new one.')
    popupInvalidIgesFileTitle = 'Error while processing file'
    popupInvalidIgesFileDescription = ('An error ocurred while processing the specified IGES file.\n' +
                                       'Please, check if the file has an .IGS or .IGES extension and ' +
                                       'try again.')

    # File Dialog Windows Strings:
    exportPcdTitle = 'Export .pcd file'
    exportPcdFormat = 'Point Cloud Data (*.pcd)'
    exportTxtTitle = 'Export .txt file'
    exportTxtFormat = 'Text File (*.txt)'
    exportScreenshotTitle = 'Export a Screenshot'
    exportScreenshotFormat = 'Image PNG (*.png)'
    importIgesTitle = 'Open an IGES file'

    # Specific Side Widget Strings:
    autoDiscretizeDescription = ('The auto discretization method will discretize all model\n' +
                                 'faces with specified parameters.')
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

    exportDescription = ('Select an export option.\n\n' +
                        'The export operations allows the generation of data\n' +
                        'files in point cloud and image formats.\n')
    exportOptionPcd = 'Export a point cloud data in .pcd'
    exportOptionTxt = 'Export a point cloud data in .txt'
    exportOptionPng = 'Export a .png screenshot'
    exportOptionDescription = ('\n.pcd (Point Cloud Data) format:\n' +
                               'default format for exporting point cloud data that\n' +
                               'can be read by most comercial softwares.\n\n' +
                               '.txt (Plain Text) format:\n' +
                               'format which contains all generated points sorted in a\n' +
                               'simple list.\n\n' +
                               '.png (Screenshot) format:\n' +
                               'Saves a screenshot of the current model in Portable\n' +
                               'Network Graphics Format.')

    faceDiscretizeDescription = ('The flat surface discretization method will discretize\n' +
                                 'according to a selection.')
    faceDiscretizeApply = 'Apply face discretization'

    importDescription = ('Select an import option.\n\n' +
                         'The import operations allows adding IGES format CAD\n' +
                         'files or a cloud data in the current visualization.\n')
    importOptionIges = 'Import an .igs or .iges file'
    importOptionPcd = 'Import a .pcd point cloud data file'

    randomDefectsDescription = ('The random defects method will apply random offsets\n' +
                                'in random directions to all selected points.')
    randomDefectsApply = 'Apply random defects'

    translationDefectsDescription = ('The translation defects method will apply specific\n' +
                                     'oriented offsets to all selected points.')
    translationDefectsApply = 'Apply translation defects'

    # General Side Widget Strings:
    flatDiscretizationHeader = '<b><br>Discretization mode for flat surfaces:</b>'
    nonFlatDiscretizationHeader = '<b><br>Discretization mode for non-flat surfaces:</b>'
    selectionModeHeader = '<b><br>Selection mode:</b>'
    entitySelectionHeader = '<b><br>Entity selection:</b>'

    gridDiscretization = 'N x N Grid Discretization'
    nonGridDiscretization = 'N points/mm Discretization'

    askingForNValue = 'Enter the value of N for discretization:'
    askingForPrecision = ('Enter the desired precision for cropping the\n' +
                         'points on curved boundary limits:')
    askingForUVDiscretization = ('Discretize non-flat surfaces using\n' +
                                 'UV Parametrization')
    askingForSelectionMethod = ('The selection method will determine which entity type\n' +
                               'will be selected in the main window.')
    askingForUParameter = 'U parameter value:'
    askingForVParameter = 'V parameter value:'
    askingForEntity = ('Select an entity which will be used to apply\n' +
                       'actions:')
    askingForDirection = ('Enter a direction (x, y, z) for applying the points\n' +
                          'translation at the selected face:')
    askingForMinimumOffset = 'Minimum offset (mm):'
    askingForMaximumOffset = 'Maximum offset (mm):'
    askingForOffset = 'Offset (mm):'
    askingForXDirection = 'X Direction:'
    askingForYDirection = 'Y Direction'
    askingForZDirection = 'Z Direction'
    selectionModeSolids = 'Solid Selection\nMode'
    selectionModeSurfaces = 'Surface Selection\nMode'
    addEntityOption = 'Add selected entity'
    useNormalDirectionOption = 'Use point-specific normal direction'
    entityPlaceholder = 'Select an entity'

    # Other Properties Strings:
    currentSessionGeneratedPoints = 'Current Session Generated Points'
    nonImplementedEntity = 'Non-Implemented Entity'

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
