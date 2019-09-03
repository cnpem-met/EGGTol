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
    applicationTitle = 'EGGTol: Error Generator for Geometric Tolerancing'
    applicationVersion = 'v2.0.0'

    # MenuBar Strings:
    menuBarFile = 'File'
    menuBarPanels = 'Panels and menus'
    menuBarVisualization = 'Visualization'
    menuBarSelection = 'Selection methods'
    menuBarAbout = 'About this application'

    # Action Strings:
    actionWelcomePrettyName = 'Welcome Panel'
    actionWelcomeStatusTip = ('Shows the welcome menu, including a short description of ' +
                             'the application')
    actionWelcomeIconText = 'Welcome!'
    actionWelcomeName = 'welcomeMenu'

    actionEntitiesPrettyName = 'Entities Panel'
    actionEntitiesStatusTip = 'Shows the entities tree'
    actionEntitiesIconText = 'Entities'
    actionEntitiesName = 'entitiesMenu'

    actionImportPrettyName = 'Import Panel'
    actionImportStatusTip = 'Import an IGES file or a point cloud file'
    actionImportIconText = 'Import'
    actionImportName = 'importMenu'

    actionExportPrettyName = 'Export Panel'
    actionExportStatusTip = 'Export a CAD model as a screenshot or a point cloud file'
    actionExportIconText = 'Export'
    actionExportName = 'exportMenu'

    actionCloudPrettyName = 'Discretization Panel'
    actionCloudStatusTip = 'Generates a point cloud for the model'
    actionCloudIconText = 'Generate Cloud'
    actionCloudName = 'cloudMenu'

    actionAutoDiscretizePrettyName = 'Auto Discretization Panel'
    actionAutoDiscretizeStatusTip = 'Generates a point cloud for the model automatically'
    actionAutoDiscretizeName = 'autoDiscretizeMenu'

    actionFaceDiscretizePrettyName = 'Flat Surface Discretization Panel'
    actionFaceDiscretizeStatusTip = ('Generates a point cloud for a specific flat surface of ' +
                                     'the model')
    actionFaceDiscretizeName = 'faceDiscretizeMenu'

    actionSurfaceDiscretizePrettyName = 'Parametric Discretization Panel'
    actionSurfaceDiscretizeStatusTip = ('Generates a point cloud for a specific non-flat ' +
                                        'surface of the model')
    actionSurfaceDiscretizeName = 'surfaceDiscretizeMenu'

    actionDefectsPrettyName = 'Deviation Generator Panel'
    actionDefectsStatusTip = 'Insert artificial deviations in point clouds'
    actionDefectsIconText = 'Apply Deviations'
    actionDefectsName = 'defectsMenu'

    actionPointsListPrettyName = 'Points Panel'
    actionPointsListStatusTip = 'Shows all the generated points in the loaded CAD model'
    actionPointsListIconText = 'List of Points'
    actionPointsListName = 'pointsMenu'

    actionLogPrettyName = 'Log Panel'
    actionLogStatusTip = 'Visualize and apply predefine actions'
    actionLogIconText = 'Log of Actions'
    actionLogName = 'logMenu'

    actionNormalVectorsPrettyName = 'Normal Vectors Panel'
    actionNormalVectorsStatusTip = "Show and manipulate the normal vectors of model's surfaces"
    actionNormalVectorsIconText = 'Normal Vectors'
    actionNormalVectorsName = 'normalVectorsMenu'

    actionTranslationPrettyName = 'Translational Deviation Panel'
    actionTranslationStatusTip = 'Insert artificial translational deviations in point clouds'
    actionTranslationName = 'translationDefectsMenu'

    actionRotationPrettyName = 'Rotational Deviation Panel'
    actionRotationStatusTip = 'Insert artificial rotational deviations in point clouds'
    actionRotationName = 'rotationDefectsMenu'

    actionRandomPrettyName = 'Random Deviation Panel'
    actionRandomStatusTip = 'Insert artificial random deviations in point clouds'
    actionRandomName = 'randomDefectsMenu'

    actionFlexionPrettyName = 'Flexion Deviation Panel'
    actionFlexionStatusTip = 'Insert Flexion perfil deviations in point clouds'
    actionFlexionName = 'FlexionDefectsMenu'

    actionPeriodicPrettyName = 'Periodic Deviation Panel'
    actionPeriodicStatusTip = 'Insert artificial periodic deviations in point clouds'
    actionPeriodicName = 'PeriodicDefectsMenu'

    actionOvalPrettyName = 'Oval Deviation Panel'
    actionOvalStatusTip = 'Insert artificial oval deviations in point clouds'
    actionOvalName = 'OvalDefectsMenu'

    actionTorsionPrettyName = 'Torsion Deviation Panel'
    actionTorsionStatusTip = 'Insert artificial torsion deviations in point clouds'
    actionTorsionName = 'TorsionDefectsMenu'

    actionSpindlePrettyName = 'Spindle Deviation Panel'
    actionSpindleStatusTip = 'Simulate a spindle deviation over a round surface'
    actionSpindleName = 'SpindleDefectsMenu'

    actionClosePrettyName = 'Close File'
    actionCloseStatusTip = 'Close the current CAD model'
    actionCloseIconText = 'Close'

    actionExitPrettyName = 'Exit'
    actionExitStatusTip = 'Quits the application'
    actionExitIconText = 'Exit'

    actionDarkPrettyName = 'Define Dark Background'
    actionDarkStatusTip = 'Configures the background with a dark color'
    actionDarkIconText = 'Dark'

    actionLightPrettyName = 'Define Light Background'
    actionLightStatusTip = 'Configures the background with a light color'
    actionLightIconText = 'Light'

    actionSelectionNeutralPrettyName = 'Solid Selection Mode'
    actionSelectionNeutralStatusTip = 'Configures the default selection mode for solids only'

    actionSelectionFacePrettyName = 'Face Selection Mode'
    actionSelectionFaceStatusTip = 'Configures the default selection mode for faces only'

    actionSelectionEdgePrettyName = 'Edge Selection Mode'
    actionSelectionEdgeStatusTip = 'Configures the default selection mode for edges only'

    actionSelectionVertexPrettyName = 'Vertex Selection Mode'
    actionSelectionVertexStatusTip = 'Configures the default selection mode for vertices only'

    actionViewTopPrettyName = 'Top View'
    actionViewTopStatusTip = 'Shows the top view of the current CAD model'
    actionViewTopIconText = 'Top View'

    actionViewBottomPrettyName = 'Bottom View'
    actionViewBottomStatusTip = 'Shows the bottom view of the current CAD model'
    actionViewBottomIconText = 'Bottom View'

    actionViewLeftPrettyName = 'Left View'
    actionViewLeftStatusTip = 'Shows the left view of the current CAD model'
    actionViewLeftIconText = 'Left View'

    actionViewRightPrettyName = 'Right View'
    actionViewRightStatusTip = 'Shows the right view of the current CAD model'
    actionViewRightIconText = 'Right View'

    actionViewFrontPrettyName = 'Front View'
    actionViewFrontStatusTip = 'Shows the front view of the current CAD model'
    actionViewFrontIconText = 'Front View'

    actionViewRearPrettyName = 'Rear View'
    actionViewRearStatusTip = 'Shows the rear view of the current CAD model'
    actionViewRearIconText = 'Rear View'

    actionViewIsoPrettyName = 'Isometric View'
    actionViewIsoStatusTip = 'Shows the isometric view of the current CAD model'
    actionViewIsoIconText = 'ISO View'

    actionWireframePrettyName = 'Wireframe CAD Mode'
    actionWireframeStatusTip = 'Shows a wireframe model of the current CAD'
    actionWireframeIconText = 'Wireframe Mode'

    actionShadedPrettyName = 'Shaded CAD Mode'
    actionShadedStatusTip = 'Shows a shaded model of the current CAD'
    actionShadedIconText = 'Shaded Mode'

    actionFitAllPrettyName = 'Fit All Elements'
    actionFitAllStatusTip = 'Adjusts the zoom level to frame all current elements'
    actionFitAllIconText = 'Fit All'

    actionGithubPrettyName = 'Open GitHub Project'
    actionGithubStatusTip = 'Shows information about this project, hosted on GitHub.com'
    actionGithubIconText = 'GitHub'

    actionDeveloperPrettyName = 'Open https://hideak.github.io'
    actionDeveloperStatusTip = 'Shows the developer webpage, including in-progress projects'
    actionDeveloperIconText = 'Dev Page'

    actionEmailPrettyName = 'Send E-mail to Developers'
    actionEmailStatusTip = 'Opens a window to send an e-mail to the developers'
    actionEmailIconText = 'E-mail'

    # Pop-up Window Strings:
    popupExitTitle = 'Quit the application'
    popupExitMessage = ('Are you sure you want to close the application?\n' +
                       'Unsaved changes will be lost.')
    popupExitButtonOK = 'Quit'
    popupExitButtonCancel = 'Cancel'

    popupCloseTitle = 'Close File'
    popupCloseMessage = ('Are you sure you want to close the file? Unsaved\n' +
                         'changes will be lost.')
    popupCloseButtonOK = 'Close'
    popupCloseButtonCancel = 'Cancel'

    popupLoadingTitle = 'Processing...'

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
                                 'Use a numeric positive integer greater than 1 for both and try again.')

    popupOpenedIgesTitle = 'IGES File is already opened'
    popupOpenedIgesDescription1 = 'The file '
    popupOpenedIgesDescription2 = (' is already opened. Finish your activities and close the current ' +
                                   'file to import a new one.')
    popupInvalidIgesFileTitle = 'Error while processing file'
    popupInvalidIgesFileDescription = ('An error ocurred while processing the specified IGES file.\n' +
                                       'Please, check if the file has an .IGS or .IGES extension and ' +
                                       'try again.')

    popupNoIgesFileTitle = 'No .IGES file was opened'
    popupNoIgesFileDescription = ('There aren\'t any active IGES file at the moment.\n' +
                                  'Please, use the IMPORT side widget to open an existing file.')

    popupNoCloudTitle = 'No point cloud was generated'
    popupNoCloudDescription = ('There aren\'t any active point cloud at the moment.\n' +
                               'Please, use the GENERATE CLOUD side widget to generate a new cloud file\n' +
                               'or use the IMPORT side widget to import an existing one.')

    popupInvalidGenericInput = 'Invalid input'
    popupInvalidGenericInputDescription = 'Invalid input value. Please, enter a valid number.'
    popupInvalidAxisComb = 'Invalid Axis combination'
    popupInvalidAxisCombDescription = 'Invalid axis combination. Please, try again with another combination.'
    popupNotRoundedSurf = 'Not rounded surface selected'
    popupNotRoundedSurfDescription = "Error: the selected surface isn't parametric (rounded)."
    popupInvalidSurf = 'Invalid selected surface'
    popupInvalidSurfDescription = 'Invalid selected surface. Please, select a discretized one to apply a deviation.'
    popupInvalidFreq = 'Invalid frequency value'
    popupInvalidFreqDescription = 'Invalid frequency value. Please, input a value different from 0.'

    popupReverseNonDiscNormSurf = 'Invalid vector reversing operation'
    popupReverseNonDiscNormSurfDescription = "Error: the selected surface isn't discretized. Please, reverse normal vectors only from discretized surfaces"

    # File Dialog Windows Strings:
    exportPcdTitle = 'Export .pcd file'
    exportPcdFormat = 'Point Cloud Data (*.pcd)'
    exportTxtTitle = 'Export .txt file'
    exportTxtFormat = 'Text File (*.txt)'
    exportScreenshotTitle = 'Export a Screenshot'
    exportScreenshotFormat = 'Image PNG (*.png)'
    importIgesTitle = 'Open an IGES file'
    importIgesFormat = 'IGES File (*.igs)'

    # Specific Side Widget Strings:
    autoDiscretizeDescription = ('The auto discretization method will discretize all model\n' +
                                 'faces with specified parameters.')
    autoDiscretizeApply = 'Apply auto discretization'

    defectsDescription = 'Select the desired transformation.'
    defectsGeneric = "----------------------------- Generic Deviations -----------------------------"
    defectsProcess = "------------------- Simulated Manufacturing Deviations -------------------"
    defectsOptionTranslation = 'Translation'
    defectsOptionRotation = 'Rotation'
    defectsOptionRandom = 'Randomic'
    defectsOptionFlexion = 'Bending'
    defectsOptionPeriodic = 'Periodic'
    defectsOptionOval = 'Oval'
    defectsOptionTorsion = 'Torsion'
    defectsOptionSpindle = 'Spindle (Turning)'
    defectsOptionMilling = 'Milling'
    defectsOptionAdditive = "Additive\nManufacturing"
    defectsOptionRectify = 'Rectify'

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

    surfaceDiscretizeDescription = ('The non-flat surface discretization method will discretize\n' +
                                    'according to a selection.')
    surfaceDiscretizeApply = 'Apply surface discretization'

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

    rotationalDefectsDescription = ('The rotational defects method will apply a specific\n' +
                                    'transformation matrix to rotate a group of points.')
    rotationalDefectsApply = 'Apply rotational defects'

    flexionDefectsDescription = ('The flexion defects method will apply a hyperbolic\n' +
                                    'perfil to the selected group of points.')
    flexionDefectsApply = 'Apply flexion defects'

    ovalDefectsDescription = ('The oval defects method will cause a flattening\n' +
                                'in a rounded discretized surface.')
    ovalDefectsApply = 'Apply oval defects'

    periodicDefectsDescription = ('The periodic defects method will apply a senoinal\n' +
                                'pattern to a discretized rounded or not rounded surface.')
    periodicDefectsApply = 'Apply periodic pattern defects'

    torsionDefectsDescription = ('The torsion defects method will cause a twist\n' +
                                'in a discretized rounded or not rounded surface.')
    torsionDefectsApply = 'Apply torsion defects'

    spindleDefectsDescription = ('Spindle deviation mode.\n\n'+
                                'Before applying the spindle deviation, follow these steps:\n'+
                                '    1. Go to the "Normal Vectors" menu\n    2. Click in "Show 3D vectors"\n'+
                                '    3. If the normal vectors of the analyzed surface are\n'+
                                '        pointing torwards inside the volume, reverse then\n'+
                                '    4. You can hide the vectors and apply the deflection now')
    spindleInfoButton = "Learn more about the implementation of this module"
    spindleDefectsApply = 'Apply spindle defects'
    spindleInfos = "Informations about the Spindle Module"
    spindleInfosDescription = "\tThis defects module was implemented using a spindle deviation model obtained with a trained Artificial Neural Network. The training dataset was acquired from a real experimental turning setup, varying cutting parameters (depth of cut, RPM, etc) and measuring the difference between the intended diameter and the real obtained after each cut. For more information about this process of moddeling, please take a look at the following works:\n [1] Bernardos et al., Prediction of Workpiece Elastic Deflections Under Cutting Forces in Turning.\n [2] Azouzi et al., On-line Prediction of Surface Finish and Dimensional Deviation in Turning Using Neural Network Based Sensor Fusion.\n\n\tTo maintain the model's accuracy, the range of the manipulated cutting parameters were limited. The same goes for the dimensions of the piece: the model will have a good prediction if the workpiece's turned surface's length and diameter are close to the values from the experimental workpiece. For now, the dimensions that will allow the good performance of the model are:\n - Length: <= 200 m\n - Diameter: 55-75 mm\n\n\tFor this reason, it is intended to collect spindle defects data from more pieces with different dimensions, to generate more models that would be automatically called to perform the deviation prediction according to the imported 3D model."

    normalVectorsDescription = 'Show and manipulate the normal vectors of\n the 3D model.\n'
    normalVectorsShow = 'Show 3D vectors'
    normalVectorsHide = 'Hide 3D vectors'
    normalVectorsReverse = 'Reverse Normal Vectors from the\nselected entity'
    normalVectorsEntitySel = 'Select an entity to manipulate its normal vectors:'

    logDescription = 'All actions, including discretization\nand deviation, showed here.'
    logSave = 'Save Log'
    logLoad = 'Load Log'
    logClean = 'Clean Log'
    logSaveMsg = 'Save log in .txt format'
    logLoadMsg = 'Load and apply actions from a saved log file'

    # General Side Widget Strings:
    flatDiscretizationHeader = '<b><br>Discretization mode for flat surfaces:</b>'
    nonFlatDiscretizationHeader = '<b><br>Discretization mode for non-flat surfaces:</b>'
    selectionModeHeader = '<b><br>Selection mode:</b>'
    entitySelectionHeader = '<b><br>Entity selection:</b>'

    gridDiscretization = 'N x N Grid Discretization'
    nonGridDiscretization = 'N points/mm Discretization'

    askingForNValue = 'Enter the value of N for discretization:'
    askingForPrecision = ('Enter the desired precision for cropping the points\n' +
                          'on curved boundary limits:')
    askingForUVDiscretization = ('Discretize non-flat surfaces using U and V\n' +
                                 'Parametrization')
    askingForSelectionMethod = ('The selection method will determine which entity type\n' +
                               'will be selected in the main window.')
    askingForUParameter = 'U parameter value:'
    askingForVParameter = 'V parameter value:'
    askingForEntity = ('Select an entity which will be used to apply actions:')
    askingForDirection = ('Enter a direction (x, y, z) for applying the points\n' +
                          'translation at the selected face:')
    askingForAngles = ('Enter a group of angles (x, y, z) that will be used\n' +
                       'to rotate the selected group of points.')
    askingForMinimumOffset = 'Minimum offset (mm):'
    askingForMaximumOffset = 'Maximum offset (mm):'
    askingForOffset = 'Offset (mm):'
    askingForXValue = 'X Value:'
    askingForYValue = 'Y Value'
    askingForZValue = 'Z Value'
    selectionModeSolids = 'Solid Selection\nMode'
    selectionModeSurfaces = 'Surface Selection\nMode'
    addEntityOption = 'Add selected entity'
    useNormalDirectionOption = 'Use point-specific normal direction'
    entityPlaceholder = 'Select an entity'

    askingForLongAxis = 'Longitudional axis:'
    askingForNormalAxis = 'Normal axis:'
    askingForMaxDev = 'Maximum deviation (mm):'
    askingForDrillAxisName = 'Periodic pattern along drill axis'
    askingForDrillAxisStatusTip = '[Circular surface]\nChecked: the points will be deflected in a periodic pattern along the drill axis\nNot checked: the points will be deflected in a periodic pattern perpendicular to the drill axis\n\n[Not circular surface]\nThis option has no effect'
    askingForAmplitude = 'Amplitude (mm):'
    askingForFrequency = 'Frequency (points/cycle):'
    askingForToolCond = 'Tool conditions:'
    askingForDepth = 'Depth of cut (mm):'
    askingForFeed = 'Feed (mm/rev):'
    askingForRPM = 'Spindle speed (RPM):'
    askingForFixtureName = 'Select the reference face of fixture'
    askingForFixtureText = 'Select the reference for fixture'
    FixtureApplyText = 'Set Fixture Face Reference'
    askingForPerpAxis = 'Perpendicular axis:'

    # Other Properties Strings:
    currentSessionGeneratedPoints = 'Current Session Generated Points'
    nonImplementedEntity = 'Non-Implemented Entity'

    # Welcome Menu Strings:
    welcomeMenuDescription = ('Welcome to the ' + applicationTitle + '!\n\n' +
                              'Version ' + applicationVersion + '\n\n' +
                              'Basic Functionality\n' +
                              '----------------------\n\n' +
                              '* To get started, make an .IGES file import using the IMPORT side widget.\n\n' +
                              '* To discretize a model, use the GENERATE CLOUD side widget.\n\n' +
                              '* To apply translational and rotational erros, use the APPLY DEVIATIONS side widget\n\n' +
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
                              'The full source code can be found through the github.com/hideak/EGGTol link.\n\n' +
                              'The source code is under the GNU free software license, and can be modifyed and distributed.')
