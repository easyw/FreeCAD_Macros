# -*- coding: utf-8 -*-

# evolution of Macro_CenterFace
# some part of Macro WorkFeature
# and assembly2
#
# center objs faces/closed_edges to first obj face/closed_edge
#
 
__title__   = "Center Faces of Parts"
__author__  = "maurice"
__url__     = "kicad stepup"
__version__ = "0.5.0" #undo alignment for App::Part hierarchical objects
__date__    = "09.2017"

testing=False #true for showing helpers
testing2=False #true for showing helpers

## todo 
#  better Gui with icons

# * (C) Maurice easyw-fc 2016
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Library General Public License (LGPL)   *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *

## done case: invert normal and standard when already aligned planes
## done works for Bodys on FC 0.17

import FreeCAD, FreeCADGui, Draft, Part, DraftTools, DraftVecUtils
from FreeCAD import Base
import sys

# Form implementation generated from reading ui file 'C:\Cad\Progetti_K\3D-FreeCad-tools\CenterAlignObjectswFacesEdges.ui'
#
# Created: Wed Sep 13 22:20:26 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CenterAlignObjectsFacesEdges(object):
    def setupUi(self, CenterAlignObjectsFacesEdges):
        CenterAlignObjectsFacesEdges.setObjectName("CenterAlignObjectsFacesEdges")
        CenterAlignObjectsFacesEdges.setWindowModality(QtCore.Qt.NonModal)
        CenterAlignObjectsFacesEdges.resize(475, 351)
        CenterAlignObjectsFacesEdges.setFocusPolicy(QtCore.Qt.NoFocus)
        self.verticalLayout = QtGui.QVBoxLayout(CenterAlignObjectsFacesEdges)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_info = QtGui.QLabel(CenterAlignObjectsFacesEdges)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lbl_info.setFont(font)
        self.lbl_info.setObjectName("lbl_info")
        self.verticalLayout_2.addWidget(self.lbl_info)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtGui.QGroupBox(CenterAlignObjectsFacesEdges)
        self.groupBox.setObjectName("groupBox")
        self.rb_bb = QtGui.QRadioButton(self.groupBox)
        self.rb_bb.setGeometry(QtCore.QRect(11, 20, 241, 20))
        self.rb_bb.setChecked(True)
        self.rb_bb.setObjectName("rb_bb")
        self.rb_mass = QtGui.QRadioButton(self.groupBox)
        self.rb_mass.setGeometry(QtCore.QRect(300, 20, 181, 20))
        self.rb_mass.setObjectName("rb_mass")
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.hLayout2 = QtGui.QHBoxLayout()
        self.hLayout2.setObjectName("hLayout2")
        self.groupBox_2 = QtGui.QGroupBox(CenterAlignObjectsFacesEdges)
        self.groupBox_2.setObjectName("groupBox_2")
        self.rb_centers = QtGui.QRadioButton(self.groupBox_2)
        self.rb_centers.setGeometry(QtCore.QRect(20, 20, 261, 20))
        self.rb_centers.setObjectName("rb_centers")
        self.rb_planes = QtGui.QRadioButton(self.groupBox_2)
        self.rb_planes.setGeometry(QtCore.QRect(20, 50, 261, 20))
        self.rb_planes.setObjectName("rb_planes")
        self.rb_centers_planes = QtGui.QRadioButton(self.groupBox_2)
        self.rb_centers_planes.setGeometry(QtCore.QRect(20, 80, 301, 20))
        self.rb_centers_planes.setChecked(True)
        self.rb_centers_planes.setObjectName("rb_centers_planes")
        self.cb_x = QtGui.QCheckBox(self.groupBox_2)
        self.cb_x.setGeometry(QtCore.QRect(370, 40, 41, 20))
        self.cb_x.setChecked(True)
        self.cb_x.setObjectName("cb_x")
        self.cb_y = QtGui.QCheckBox(self.groupBox_2)
        self.cb_y.setGeometry(QtCore.QRect(370, 60, 41, 20))
        self.cb_y.setChecked(True)
        self.cb_y.setObjectName("cb_y")
        self.cb_z = QtGui.QCheckBox(self.groupBox_2)
        self.cb_z.setGeometry(QtCore.QRect(370, 80, 41, 20))
        self.cb_z.setChecked(True)
        self.cb_z.setObjectName("cb_z")
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(350, 20, 61, 16))
        self.label_2.setObjectName("label_2")
        self.hLayout2.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.hLayout2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cb_inv_normals = QtGui.QCheckBox(CenterAlignObjectsFacesEdges)
        self.cb_inv_normals.setObjectName("cb_inv_normals")
        self.verticalLayout_3.addWidget(self.cb_inv_normals)
        self.line = QtGui.QFrame(CenterAlignObjectsFacesEdges)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.label = QtGui.QLabel(CenterAlignObjectsFacesEdges)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.hLayout1 = QtGui.QHBoxLayout()
        self.hLayout1.setObjectName("hLayout1")
        self.btnAlign = QtGui.QPushButton(CenterAlignObjectsFacesEdges)
        self.btnAlign.setObjectName("btnAlign")
        self.hLayout1.addWidget(self.btnAlign)
        self.btnMove = QtGui.QPushButton(CenterAlignObjectsFacesEdges)
        self.btnMove.setObjectName("btnMove")
        self.hLayout1.addWidget(self.btnMove)
        self.btnUndoMove = QtGui.QPushButton(CenterAlignObjectsFacesEdges)
        self.btnUndoMove.setObjectName("btnUndoMove")
        self.hLayout1.addWidget(self.btnUndoMove)
        self.verticalLayout_3.addLayout(self.hLayout1)
        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(CenterAlignObjectsFacesEdges)
        QtCore.QMetaObject.connectSlotsByName(CenterAlignObjectsFacesEdges)

    def retranslateUi(self, CenterAlignObjectsFacesEdges):
        CenterAlignObjectsFacesEdges.setWindowTitle(QtGui.QApplication.translate("CenterAlignObjectsFacesEdges", "Center Align Faces/Edges", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_info.setText(QtGui.QApplication.translate("CenterAlignObjectsFacesEdges", "<html><head/><body><p>Select [Ctrl+Click] multiple face(s) or closed Edges<br>or Planes or Axis and click Align</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("CenterAlignObjectsFacesEdges", "reference", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_bb.setText(QtGui.QApplication.translate("CenterAlignObjectsFacesEdges", "Center of Bounding Box", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_mass.setText(QtGui.QApplication.translate("CenterAlignObjectsFacesEdges", "Center of Mass", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("CenterAlignObjectsFacesEdges", "aligning", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_centers.setText(QtGui.QApplication.translate("CenterAlignObjectsFacesEdges", "Align Faces/Edges Centers", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_planes.setText(QtGui.QApplication.translate("CenterAlignObjectsFacesEdges", "Align Faces/Edges Planes", None, QtGui.QApplication.UnicodeUTF8))
        self.rb_centers_planes.setText(QtGui.QApplication.translate("CenterAlignObjectsFacesEdges", "Align Faces/Edges Centers and Planes", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_x.setText(QtGui.QApplication.translate("CenterAlignObjectsFacesEdges", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_y.setText(QtGui.QApplication.translate("CenterAlignObjectsFacesEdges", "y", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_z.setText(QtGui.QApplication.translate("CenterAlignObjectsFacesEdges", "z", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CenterAlignObjectsFacesEdges", "center on:", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_inv_normals.setText(QtGui.QApplication.translate("CenterAlignObjectsFacesEdges", "invert Normal for Plane", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CenterAlignObjectsFacesEdges", "<html><b>First Face/Edge is the Reference for alignment</b>&nbsp;&nbsp;&nbsp;<u>vers. 0.4.9</u>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAlign.setToolTip(QtGui.QApplication.translate("CenterAlignObjectsFacesEdges", "select Faces or Edges (Ctrl+LBM) and click button to Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAlign.setText(QtGui.QApplication.translate("CenterAlignObjectsFacesEdges", "Align", None, QtGui.QApplication.UnicodeUTF8))
        self.btnMove.setToolTip(QtGui.QApplication.translate("CenterAlignObjectsFacesEdges", "select an Object and click button to Move it", None, QtGui.QApplication.UnicodeUTF8))
        self.btnMove.setText(QtGui.QApplication.translate("CenterAlignObjectsFacesEdges", "Move", None, QtGui.QApplication.UnicodeUTF8))
        self.btnUndoMove.setToolTip(QtGui.QApplication.translate("CenterAlignObjectsFacesEdges", "select Faces / Edges and click to show Normals", None, QtGui.QApplication.UnicodeUTF8))
        self.btnUndoMove.setText(QtGui.QApplication.translate("CenterAlignObjectsFacesEdges", "undo", None, QtGui.QApplication.UnicodeUTF8))

### ------------------------------------------------------------------------------------ ###
### ---------code to be inserted and remove from new generation------------------------- ###
### ------------------------------------------------------------------------------------ ###
        self.btnAlign.clicked.connect(self.onAlign)
        self.btnMove.clicked.connect(self.onMove)
        self.btnUndoMove.clicked.connect(self.onUndo)
        
    def onAlign(self):
        say("Align clicked")
        normal=0;type=0;mode=0
        if self.cb_inv_normals.isChecked():
            say("Align Normal Inverted")
            normal=1
        if self.rb_bb.isChecked():
            say("centering on Bounding Boxes")
        else:
            say("centering on Center of Mass")
            type=1
        if self.rb_centers_planes.isChecked():
            say("Centering and aligning Planes")
        elif self.rb_centers.isChecked():
            say("Centering Faces/Edges")
            mode=1
        else:
            say("Aligning Planes")
            mode=2
        cx=0;cy=0;cz=0
        if self.cb_x.isChecked():
            cx=1
        if self.cb_y.isChecked():
            cy=1
        if self.cb_z.isChecked():
            cz=1
        Align(normal,type,mode,cx,cy,cz)

    def onMove(self):
        say("Move clicked")
        Move()
        say("Move clicked2")

    def onUndo(self):
        say("Undo clicked")
        Undo()
        say("Undo clicked2")

##############################################################
global initial_placement, last_selection
global moving, rotating
global objs_moved, plc_moved

    
#init
initial_placement = FreeCAD.Placement(App.Vector(0,0,0), App.Rotation(0,0,0), App.Vector(0,0,0)) #Placement [Pos=(0,0,0), Yaw-Pitch-Roll=(0,0,0)]
moving = [] #[App.Vector(0,0,0)]
rotating = [] #[0, App.Vector(0,0,0), App.Vector(0,0,0)]
objs_moved = []
plc_moved = []
#Draft.rotate(objs[j],-rot_angle,rot_center,rot_axis)
#rotating=[rot_angle,rot_center,rot_axis]

last_selection = []      

def say(msg):
    FreeCAD.Console.PrintMessage(msg)
    FreeCAD.Console.PrintMessage('\n')

def sayw(msg):
    FreeCAD.Console.PrintWarning(msg)
    FreeCAD.Console.PrintWarning('\n')

def sayerr(msg):
    FreeCAD.Console.PrintError(msg)
    FreeCAD.Console.PrintWarning('\n')

def make_string(input):
    if (sys.version_info > (3, 0)):  #py3
        if isinstance(input, str):
            return input
        else:
            input =  input.encode('utf-8')
            return input
    else:  #py2
        if type(input) == unicode:
            input =  input.encode('utf-8')
            return input
        else:
            return input

def singleInstance():
    app = QtGui.qApp

    for i in app.topLevelWidgets():
        if i.objectName() == "CenterAlignObjectsFacesEdges":
            i.deleteLater()
        else:
            pass

## assigning DisplayModeBody to Tip to attach Facebinder to Body
doc=FreeCAD.ActiveDocument
#Init        
   
    
singleInstance()

CenterAlignObjectsFacesEdges = QtGui.QWidget()
ui = Ui_CenterAlignObjectsFacesEdges()
ui.setupUi(CenterAlignObjectsFacesEdges)
#CenterAlignObjectsFacesEdges.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
CenterAlignObjectsFacesEdges.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint & QtCore.Qt.WindowTitleHint & QtCore.Qt.WindowMinimizeButtonHint & QtCore.Qt.WindowSystemMenuHint & QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowStaysOnTopHint);
## CenterAlignObjectsFacesEdges.setWindowFlags(CenterAlignObjectsFacesEdges.windowFlags() & QtCore.Qt.CustomizeWindowHint)
#CenterAlignObjectsFacesEdges.setWindowModality(QtCore.Qt.ApplicationModal)
#self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
#CenterAlignObjectsFacesEdges.setWindowFlags(CenterAlignObjectsFacesEdges.windowFlags() & QtCore.Qt.WindowStaysOnTopHint)
CenterAlignObjectsFacesEdges.show()

# def center(self):
#     frameGm = self.frameGeometry()
#     screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
#     #say(screen)
#     centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
#     #say(centerPoint)
#     frameGm.moveCenter(centerPoint)
#     self.move(frameGm.center)

#center(CenterAlignObjectsFacesEdges)
if not testing:
    CenterAlignObjectsFacesEdges.move(100,100)
else:
    CenterAlignObjectsFacesEdges.move(500,100)
## to do:
## ok single instance
## - always on top
## - no maximize
### ------------------------------------------------------------------------------------ ###
### ---------code to be inserted and remove from new generation------------------------- ###
### ------------------------------------------------------------------------------------ ###


def Undo():
    say('Undo')
    global initial_placement, last_selection
    global moving, rotating
    global objs, objs_plc
    global objs_moved, plc_moved

    if len(last_selection) == 1:
        obj = last_selection[0].Object
        say ('last selection: ' + obj.Name)
        #obj.Placement.Base =initial_placement
        obj.Placement = initial_placement
        FreeCAD.ActiveDocument.recompute()
        objs = []
        last_selection = []
    elif len (objs) > 1:
        say ('Moving: ' + str(moving))
        say ('Rotating: ' + str(rotating))
        #sayerr(len(objs_moved))
        i=0
        for o in objs_moved:
            #sayerr (o.Name)
            #sayerr (plc_moved[i])
            o.Placement = plc_moved[i]
            i=i+1
            
        objs = []
        last_selection = []
        objs_moved = []
        plc_moved = []
        FreeCAD.ActiveDocument.recompute()
    
def Move():
    global initial_placement, last_selection
    global objs, objs_plc
    
    say('Move')
    selection = [s for s in FreeCADGui.Selection.getSelectionEx() if s.Document == FreeCAD.ActiveDocument ]
    if len(selection) == 1:
        objs = []
        last_selection = selection
        say('Move2')
        PartMover( FreeCADGui.activeDocument().activeView(), selection[0].Object )
        say('starting '+str(initial_placement))
    else:
        PartMoverSelectionObserver()

class PartMover:
    global initial_placement
    
    def __init__(self, view, obj):
        global initial_placement
        self.obj = obj
        self.initialPosition = self.obj.Placement.Base
        initial_placement = self.initialPosition
        #sayw('init '+str(initial_placement))
        self.copiedObject = False
        self.view = view
        self.callbackMove = self.view.addEventCallback("SoLocation2Event",self.moveMouse)
        self.callbackClick = self.view.addEventCallback("SoMouseButtonEvent",self.clickMouse)
        self.callbackKey = self.view.addEventCallback("SoKeyboardEvent",self.KeyboardEvent)
    def moveMouse(self, info):
        newPos = self.view.getPoint( *info['Position'] )
        # debugPrint(5, 'new position %s' % str(newPos))
        self.obj.Placement.Base = newPos
    def removeCallbacks(self):
        self.view.removeEventCallback("SoLocation2Event",self.callbackMove)
        self.view.removeEventCallback("SoMouseButtonEvent",self.callbackClick)
        self.view.removeEventCallback("SoKeyboardEvent",self.callbackKey)
    def clickMouse(self, info):
        global initial_placement
        # debugPrint(4, 'clickMouse info %s' % str(info))
        if info['Button'] == 'BUTTON1' and info['State'] == 'DOWN':
            if not info['ShiftDown'] and not info['CtrlDown']:
                say('releasing obj')
                FreeCAD.ActiveDocument.recompute()
                #sayw('releasing\ninitial p: '+ str( initial_placement ))
                #sayw('final p: '+str(self.obj.Placement.Base))
                self.removeCallbacks()
            elif info['ShiftDown']: #copy object
                self.obj = duplicateImportedPart( self.obj )
                self.copiedObject = True
            elif info['CtrlDown']:
                azi   =  ( numpy.random.rand() - 0.5 )*numpy.pi*2
                ela   =  ( numpy.random.rand() - 0.5 )*numpy.pi
                theta =  ( numpy.random.rand() - 0.5 )*numpy.pi
                axis = azimuth_and_elevation_angles_to_axis( azi, ela )
                self.obj.Placement.Rotation.Q = quaternion( theta, *axis )

    def KeyboardEvent(self, info):
        # debugPrint(4, 'KeyboardEvent info %s' % str(info))
        if info['State'] == 'UP' and info['Key'] == 'ESCAPE':
            if not self.copiedObject:
                self.obj.Placement.Base = self.initialPosition
            else:
                FreeCAD.ActiveDocument.removeObject(self.obj.Name)
            self.removeCallbacks()

class PartMoverSelectionObserver:
     def __init__(self):
         FreeCADGui.Selection.addObserver(self)
         FreeCADGui.Selection.removeSelectionGate()
     def addSelection( self, docName, objName, sub, pnt ):
         # debugPrint(4,'addSelection: docName,objName,sub = %s,%s,%s' % (docName, objName, sub))
         FreeCADGui.Selection.removeObserver(self)
         obj = FreeCAD.ActiveDocument.getObject(objName)
         view = FreeCADGui.activeDocument().activeView()
         PartMover( view, obj )

# class MovePartCommand:
#     say('Move')
#     def Activated(self):
#         selection = [s for s in FreeCADGui.Selection.getSelectionEx() if s.Document == FreeCAD.ActiveDocument ]
#         if len(selection) == 1:
#             say('Move2')
#             PartMover( FreeCADGui.activeDocument().activeView(), selection[0].Object )
#         else:
#             PartMoverSelectionObserver()

#FreeCADGui.addCommand('assembly2_movePart', MovePartCommand())
            
def duplicateImportedPart( part ):
    nameBase = part.Label
    while nameBase[-1] in '0123456789' and len(nameBase) > 0:
        nameBase = nameBase[:-1]
    try:
        newObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", findUnusedObjectName(nameBase))
    except UnicodeEncodeError:
        safeName = findUnusedObjectName('import_')
        newObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", safeName)
        newObj.Label = findUnusedLabel( nameBase )
    newObj.addProperty("App::PropertyFile",    "sourceFile",    "importPart").sourceFile = part.sourceFile
    newObj.addProperty("App::PropertyFloat", "timeLastImport","importPart").timeLastImport =  part.timeLastImport
    newObj.setEditorMode("timeLastImport",1)
    newObj.addProperty("App::PropertyBool","fixedPosition","importPart").fixedPosition = False# part.fixedPosition
    newObj.addProperty("App::PropertyBool","updateColors","importPart").updateColors = getattr(part,'updateColors',True)
    newObj.Shape = part.Shape.copy()
    for p in part.ViewObject.PropertiesList: #assuming that the user may change the appearance of parts differently depending on their role in the assembly.
        if hasattr(newObj.ViewObject, p) and p not in ['DiffuseColor','Proxy']:
            setattr(newObj.ViewObject, p, getattr( part.ViewObject, p))
    newObj.ViewObject.DiffuseColor = copy.copy( part.ViewObject.DiffuseColor )
    newObj.Proxy = Proxy_importPart()
    newObj.ViewObject.Proxy = ImportedPartViewProviderProxy()
    newObj.Placement.Base = part.Placement.Base
    newObj.Placement.Rotation = part.Placement.Rotation
    return newObj    

def recurse_node(obj,plcm,scl):
    sayerr(obj.Name)
    if "App::Part" in obj.TypeId or "Body" in obj.TypeId or "Compound" in obj.TypeId:
        for o in obj.Group:
            #sayerr(o.Name)
            if "App::Part" in o.TypeId  or "Body" in o.TypeId or "Compound" in o.TypeId:
                #sayerr(o.Name)#+" * "+obj.Name)
                new_plcm=get_node_plc(o,obj)
                recurse_node(o,new_plcm,scl)
            else:
                if "Sketcher" not in o.TypeId:
                    simple_cpy_plc(o,plcm)
                    scl.append(FreeCAD.ActiveDocument.ActiveObject)
##

def get_top_level (obj):
    lvl=10000
    for ap in obj.InListRecursive:
        if len(ap.InListRecursive) < lvl:
            top = ap
            lvl = len(ap.InListRecursive)
    return top

def reset_prop_shapes(obj):

    s=obj.Shape
    #say('resetting props #2')
    r=[]
    t=s.copy()
    for i in t.childShapes():
        c=i.copy()
        c.Placement=t.Placement.multiply(c.Placement)
        r.append((i,c))

    w=t.replaceShape(r)
    w.Placement=FreeCAD.Placement()
    Part.show(w)
    #say(w)
    #
    #FreeCADGui.ActiveDocument.ActiveObject.ShapeColor=FreeCADGui.ActiveDocument.Part__Feature.ShapeColor
    #FreeCADGui.ActiveDocument.ActiveObject.LineColor=FreeCADGui.ActiveDocument.Part__Feature.LineColor
    #FreeCADGui.ActiveDocument.ActiveObject.PointColor=FreeCADGui.ActiveDocument.Part__Feature.PointColor
    #FreeCADGui.ActiveDocument.ActiveObject.DiffuseColor=FreeCADGui.ActiveDocument.Part__Feature.DiffuseColor
    FreeCADGui.ActiveDocument.ActiveObject.ShapeColor=FreeCADGui.ActiveDocument.getObject(obj.Name).ShapeColor
    FreeCADGui.ActiveDocument.ActiveObject.LineColor=FreeCADGui.ActiveDocument.getObject(obj.Name).LineColor
    FreeCADGui.ActiveDocument.ActiveObject.PointColor=FreeCADGui.ActiveDocument.getObject(obj.Name).PointColor
    FreeCADGui.ActiveDocument.ActiveObject.DiffuseColor=FreeCADGui.ActiveDocument.getObject(obj.Name).DiffuseColor
    new_label=obj.Label
    FreeCAD.ActiveDocument.removeObject(obj.Name)
    FreeCAD.ActiveDocument.recompute()
    FreeCAD.ActiveDocument.ActiveObject.Label=new_label
    rstObj=FreeCAD.ActiveDocument.ActiveObject
    #say(rstObj)
    #

    return rstObj

def Align(normal,type,mode,cx,cy,cz):
    global initial_placement, last_selection
    global objs, objs_plc
    global moving, rotating
    global objs_moved, plc_moved
    objs = [] ; objs_plc = []
    objs_moved = [] ; plc_moved = []
    
    
    #cx = 1  # center x -> 1  
    #cy = 1  # center y -> 1 
    #cz = 1  # center z -> 1 
    say(str(cx)+str(cy)+str(cz))
    create_points=False
    use_bb = True #align center based on bounding boxes or center of mass
    if type==1:
        use_bb = False #align center based on bounding boxes or center of mass

    sel = FreeCADGui.Selection.getSelection()
    selEx = FreeCADGui.Selection.getSelectionEx()
    if len(selEx) < 2 and not testing:
        return
    last_selection = []
    say("number of objects: "+ str(len(selEx)))
    objs = [selobj.Object for selobj in selEx]
    #k=0
    for o in objs:
        say ('obj: ' + o.Name)
        objs_plc.append(o.Placement) #.Base)
        say ('Placement: ' + str(o.Placement)) #.Base))
        moving.append([App.Vector(0,0,0)])
        rotating.append([0, App.Vector(0,0,0), App.Vector(0,0,0)])
        #k=k+1
        
    def edgeToVector(edge):
        """ Return a vector from an edge or a Part.line.
        """
        if isinstance(edge,Part.Shape):
            return edge.Vertexes[-1].Point.sub(edge.Vertexes[0].Point)
        elif isinstance(edge,Part.Line):
            return edge.EndPoint.sub(edge.StartPoint)
        else:
            sayw("Error in edgeToVector(edge) : not a good type of input" + str(type(edge)))
            return None    

    def centerLinePoint(edge,info=0):
        """ Return the center point of the Line.
        """
        center = None
        #VVector_A=edge.valueAt( 0.0 )
        Vector_A = edge.Vertexes[0].Point
        if info != 0:
            say("Origin of line selected is : "+str(Vector_A)) 
        #Vector_B=edge.valueAt( edge.Length )
        Vector_B = edge.Vertexes[-1].Point
        if info != 0:
            say("End of line selected is : "+str(Vector_B)) 
        Vector_MidPoint = Vector_B + Vector_A
        center = Vector_MidPoint.multiply(0.5)
        if info != 0:
            say("Center of line selected is : "+str(center)) 
        return center
    
    def object_alignEdges():
        """ 
        Align the Edge(s) from selected object(s) to the last Edge selected.
        - Click first to select an Edge of an object or several Edges from several objects. 
        - Click second to select an Edge to align to.
    
        NB:
        The center of rotation is the center of the bounbing box if possible or 
        the center of the Edge.
        
        if the Edge of the object selected is already aligned to the last one,
        a rotation of 180 deg is applied to the object.
        In this case the Axis of rotation is Z vector : Base.Vector(0, 0, 1)
        
        Two clicks will rotate by 180 deg.
        """
        msg=verbose
    
        error_msg =\
        "INCORRECT Object(s) Selection :\n" +\
        "You Must Select at least two(2) Edges (from two objects) !\n" +\
        "All Edges will be aligned to the last one !"
        
        Selection = get_SelectedObjectsWithParent(info=msg, printError=False)
        m_actDoc=get_ActiveDocument(info=1)
        Selection2 = Gui.Selection.getSelectionEx(m_actDoc.Name)
        
        try:
            SelectedObjects = Selection
            Number_of_Edges  = SelectedObjects[1]
            if msg!=0:
                print_msg("Number_of_Edges=" + str(Number_of_Edges))
                
            if Number_of_Edges >= 2 :
                Edge_List = SelectedObjects[4]
                if msg != 0:
                    print_msg(" Edge_List=" + str(Edge_List))
                
                # Get the Reference Edge : last of the selected
                Ref_Edge_dict = Edge_List[-1]
                for Selected_Edge, Parent_Edge in Ref_Edge_dict.iteritems():
                    Edge_ref = Selected_Edge
    
                del Edge_List[-1]
                            
                for Selected_Edge_dict in Edge_List:
                    if msg != 0:
                        print_msg("Selected_Edge_dict = " + str(Selected_Edge_dict))
                    for Selected_Edge, Parent_Edge in Selected_Edge_dict.iteritems():
                        if msg != 0:
                            print_msg("Selected_Edge = " + str(Selected_Edge))
                            print_msg("Parent = " + str(Parent_Edge))
                        try:                        
                            Edge_Point = Parent_Edge.Shape.BoundBox.Center
                        except:
                            Edge_Point = centerLinePoint(Selected_Edge,info=0)
                        
                        if msg != 0:
                            print_point(Edge_Point, msg="Edge_Point = ")
                        Edge = Selected_Edge
                        
                        if colinearEdges(Edge, Edge_ref, info=msg , tolerance=1e-12):
                            rot_axis = Base.Vector(0, 0, 1).cross(edgeToVector(Edge))
                            rot_center = Edge_Point
                            rot_angle = 180. + m_angleAlignEdges
                            Draft.rotate(Parent_Edge,rot_angle,rot_center,rot_axis)
                        else:
                            m_angle, m_angle_rad = angleBetween(Edge,Edge_ref)
                            print_msg("m_angle = " + str(m_angle))
                            rot_axis = edgeToVector(Edge).cross(edgeToVector(Edge_ref))
                            print_msg("rot_axis = " + str(rot_axis))
                            rot_center = Edge_Point
                            rot_angle = m_angle + m_angleAlignEdges
                            Draft.rotate(Parent_Edge,rot_angle,rot_center,rot_axis)
                # Reset the selection changed by Draft.rotate 
                reset_SelectedObjects(Selection2, info=0)
            else:
                sayerr(error_msg)                          
        except:
            sayerr(error_msg)
    
    
    def angleBetween(e1, e2):
        """ Return the angle (in degrees) between 2 edges.
        """
        if isinstance(e1,Part.Edge) and isinstance(e2,Part.Edge):
            # Create the Vector for first edge
            v1 = e1.Vertexes[-1].Point
            v2 = e1.Vertexes[0].Point
            ve1 = v1.sub(v2)
            # Create the Vector for second edge
            v3 = e2.Vertexes[-1].Point
            v4 = e2.Vertexes[0].Point
            ve2 = v3.sub(v4)
        elif isinstance(e1,Base.Vector) and isinstance(e2,Base.Vector):
            ve1 = e1
            ve2 = e2
        elif isinstance(e1,Part.Edge) and isinstance(e2,Base.Vector):
            v1 = e1.Vertexes[-1].Point
            v2 = e1.Vertexes[0].Point
            ve1 = v1.sub(v2)
            ve2 = e2
        elif isinstance(e1,Base.Vector) and  isinstance(e2,Part.Edge):
            ve1 = e1
            v3 = e2.Vertexes[-1].Point
            v4 = e2.Vertexes[0].Point
            ve2 = v3.sub(v4)   
        else:
            return
        
        angle = ve1.getAngle(ve2)
        import math
        return math.degrees(angle), angle
        
    def colinearVectors(A, B, C, info=0, tolerance=1e-12):
        """ Return true if the 3 points are aligned.
        """
        Vector_1 = B - A
        Vector_2 = C - B
        #if info != 0:
        #    print_point(Vector_1, msg="Vector_1 : ")
        #    print_point(Vector_2, msg="Vector_2 : ")
        Vector_3 = Vector_1.cross(Vector_2)
        #if info != 0:
        #    print_point(Vector_3, msg="Vector_1.cross(Vector_2) : ")
            
        if abs(Vector_3.x) <= tolerance and abs(Vector_3.y) <= tolerance and abs(Vector_3.z) <= tolerance:
            if info != 0:
                sayw("Colinear Vectors !")
            return True
        else:
            if info != 0:
                sayw("NOT Colinear Vectors !")
            return False
        return 
    
    coords = []
    normals = []
    coordPs = []
    sEdge = []
    j = 0
    p0 =  FreeCAD.Placement (FreeCAD.Vector(0,0,0), FreeCAD.Rotation(0,0,0), FreeCAD.Vector(0,0,0))
    # .BoundBox.Center
    #align faces
    if (len(selEx) > 1) and (len(selEx)==len(sel)):
        #s = obj.Shape
        last_selection = [] #removing old Move object
        top_level_obj=[]
        
        for i in range (len(selEx)):
            top_level_obj.append('none')
        for fc in selEx:
            say ("j= "+str(j))
            say("len selEx "+str(len(selEx)))
            s=fc
            #selectedEdge = FreeCADGui.Selection.getSelectionEx()[j].SubObjects[0] # select one element SubObjects    
            if (selEx[j].Object.TypeId == 'App::Plane') or (selEx[j].Object.TypeId == 'PartDesign::Plane'):
                cw = Part.Wire([Part.Circle(FreeCAD.Vector(0, 0), FreeCAD.Vector(0, 0, 1), 2.0).toShape()])
                fp = Part.Face(cw)
                pad=0
                edge_op=0
                f=fp.copy()
                Part.show(f)
                #FreeCAD.ActiveDocument.removeObject("TempPlane")
                FreeCAD.ActiveDocument.recompute()
                fName= FreeCAD.ActiveDocument.ActiveObject.Name
                f.Placement=selEx[j].Object.Placement #.multiply(FreeCAD.ActiveDocument.getObject(fName).Placement)
                s = FreeCAD.ActiveDocument.getObject(fName)
                s.Placement = f.Placement
                sayerr(str(f.Placement))
                s.Label = 'single-copy-absolute-placement'
                #f.Placement = s.Placement
                say("Label : "+ make_string(sel[j].Label))     # extract the Label
                say("Name  : "+ str(sel[j].Name))     # extract the Name
                say( "Center Face Binder "+str(0)+" "+str(f.Faces[0].CenterOfMass)) # Vector center mass to face
                say( "Center Face Binder bb "+str(0)+" "+str(f.Faces[0].BoundBox.Center)) # Vector center mass to face
            elif (selEx[j].Object.TypeId == 'App::Line') or (selEx[j].Object.TypeId == 'PartDesign::Line'):
                FreeCAD.ActiveDocument.addObject("Part::Plane","TempAxis")
                FreeCAD.ActiveDocument.TempAxis.Length=5.000
                FreeCAD.ActiveDocument.TempAxis.Width=5.000
                FreeCAD.ActiveDocument.TempAxis.Placement=selEx[j].Object.Placement
                #FreeCAD.ActiveDocument.TempAxis.Placement.Base=\
                #  (-FreeCAD.ActiveDocument.TempAxis.Shape.BoundBox.Center.x,-FreeCAD.ActiveDocument.TempAxis.Shape.BoundBox.Center.y,-FreeCAD.ActiveDocument.TempAxis.Shape.BoundBox.Center.z)
                ##FreeCAD.ActiveDocument.TempPlane.Placement=selEx[j].Object.Placement
                #FreeCAD.ActiveDocument.TempAxis.Placement=selEx[j].Object.Placement.multiply(FreeCAD.ActiveDocument.TempAxis.Placement)
                FreeCAD.ActiveDocument.TempAxis.Label='TempAxis'
                FreeCAD.ActiveDocument.recompute()
                #t1=FreeCAD.ActiveDocument.TempAxis.Shape
                #Part.show(t1)
                fp = FreeCAD.ActiveDocument.TempAxis.Shape.Faces[0].Edges[1]
                pad=0
                edge_op=2
                f=fp.copy()
                Part.show(f)
                #stop
                FreeCAD.ActiveDocument.removeObject("TempAxis")
                FreeCAD.ActiveDocument.recompute()
                fName= FreeCAD.ActiveDocument.ActiveObject.Name
                s = FreeCAD.ActiveDocument.getObject(fName)
                s.Placement = f.Placement
                sayerr(str(f.Placement))
                s.Label = 'single-copy-absolute-placement'
                #f.Placement = s.Placement
                say("Label : "+ make_string(sel[j].Label))     # extract the Label
                say("Name  : "+ str(sel[j].Name))     # extract the Name
                say( "Center Face Binder "+str(0)+" "+str(f.CenterOfMass)) # Vector center mass to face
                say( "Center Face Binder bb "+str(0)+" "+str(f.BoundBox.Center)) # Vector center mass to face
            else:
                try:
                    selectedEdge = selEx[j].SubObjects[0] # select one element SubObjects    
                except:
                    sayerr('select only Faces or closed Edges')
                    return
                sEdge.append(selectedEdge)
                pad=0
                edge_op=0
                if str(fc.SubObjects[0])[1:5] != "Face": #edge
                    # try:                        
                    #     Edge_Point = centerLinePoint(selectedEdge,info=1)
                    # except:
                    #     stop
                    try:
                        sayerr(str(selectedEdge.Placement))
                        wire = Part.Wire(selectedEdge)
                        #sayw(str(wire.Placement))
                        e = selectedEdge
                        f = Part.Face(wire)
                    except: # edge not closed
                        wire = Part.Wire(selectedEdge)
                        f = wire
                        edge_op=1
                        #sayerr('edge not closed to be managed')
                        Edge_Point = centerLinePoint(selectedEdge,info=0)
                        #reply = QtGui.QMessageBox.information(None,"info", "edge(s) non closed are not managed atm\n")
                        #stop
                    #Part.show(fw)
                    Part.show(f)
                    #stop
                    #f.Placement=selectedEdge.Placement
                    fName= FreeCAD.ActiveDocument.ActiveObject.Name
                    s = FreeCAD.ActiveDocument.getObject(fName)
                    #sayerr(str(f.Placement))
                    s.Placement = f.Placement
                    s.Label = 'single-copy-absolute-placement-edge'
                    #stop
                    #f.Placement = s.Placement
                    pad=1
                    #FreeCAD.ActiveDocument.recompute()
                    say("Label : "+ make_string(sel[j].Label))     # extract the Label
                    say("Name  : "+ str(sel[j].Name))     # extract the Name
                    if edge_op==0:
                        say( "Center Face Binder "+str(0)+" "+str(f.Faces[0].CenterOfMass)) # Vector center mass to face
                        say( "Center Face Binder bb "+str(0)+" "+str(f.Faces[0].BoundBox.Center)) # Vector center mass to face
                    else:
                        say( "Center Face Binder "+str(0)+" "+str(f.CenterOfMass)) # Vector center mass to face
                        say( "Center Face Binder bb "+str(0)+" "+str(f.BoundBox.Center)) # Vector center mass to face
                else: #face
                    pad=0
                    f=fc.SubObjects[0].Faces[0].copy()
                    Part.show(f)
                    fName= FreeCAD.ActiveDocument.ActiveObject.Name
                    s = FreeCAD.ActiveDocument.getObject(fName)
                    s.Placement = f.Placement
                    sayerr(str(f.Placement))
                    s.Label = 'single-copy-absolute-placement'
                    #f.Placement = s.Placement
                    say("Label : "+ make_string(sel[j].Label))     # extract the Label
                    say("Name  : "+ str(sel[j].Name))     # extract the Name
                    say( "Center Face Binder "+str(0)+" "+str(f.Faces[0].CenterOfMass)) # Vector center mass to face
                    say( "Center Face Binder bb "+str(0)+" "+str(f.Faces[0].BoundBox.Center)) # Vector center mass to face
            # LineColor
            ob = fc.Object
            #print ob.Placement
            ## pOriginal=ob.Placement
            pOriginal=f.Placement
            s.Placement=p0
            #stop
            ##ob.Placement=p0
            #say('resetting props #2')
            #sh=ob.Shape
            sh=s.Shape
            r=[]
            t=sh.copy()
            for i in t.childShapes():
                c=i.copy()
                c.Placement=t.Placement.multiply(c.Placement)
                r.append((i,c))
            acpy=t.replaceShape(r)
            acpy.Placement=FreeCAD.Placement()
            if hasattr(ob,'InListRecursive'):
                lrl=len(ob.InListRecursive)
                for o in ob.InListRecursive:
                    say(o.Name)
                inverted=True
                if len(ob.InList):
                    top_level_obj[j] = get_top_level(ob)
                    #sayerr(top_level_obj[j].Label)
                    #stop
                    if ob.InListRecursive[0].Name == ob.InList[0].Name:
                        inverted=False
                    if inverted:
                        #top_level_obj[j]=(ob.InListRecursive[0])
                        for i in range (0,lrl):
                            if hasattr(ob.InListRecursive[i],'Placement'):
                                acpy.Placement=acpy.Placement.multiply(ob.InListRecursive[i].Placement)
                    else:
                        #top_level_obj[j]=(ob.InListRecursive[lrl-1])
                        for i in range (0,lrl):
                            if hasattr(ob.InListRecursive[lrl-1-i],'Placement'):
                                acpy.Placement=acpy.Placement.multiply(ob.InListRecursive[lrl-1-i].Placement)
            say(acpy.Placement)
            #acpy.Placement=acpy.Placement.multiply(pOriginal)
            if pad == 0: #note making wire from edge already resets the original placement
                acpy.Placement=acpy.Placement.multiply(pOriginal)
            s.Placement = acpy.Placement
            ##ob.Placement = pOriginal
            #stop
            f.Placement = s.Placement
            #stop
        
            red   = 1.0  # 1 = 255
            green = 0.0  #
            blue  = 0.0  #
            if create_points:
                if pad==0:
                    if use_bb:
                        Draft.makePoint(f.Faces[0].BoundBox.Center.x,f.Faces[0].BoundBox.Center.y,f.Faces[0].BoundBox.Center.z) # create a point
                    else:
                        Draft.makePoint(f.Faces[0].CenterOfMass.x,f.Faces[0].CenterOfMass.y,f.Faces[0].CenterOfMass.z) # create a point
                    FreeCADGui.activeDocument().activeObject().PointColor = (red, green, blue)
                else:
                    if use_bb:
                        Draft.makePoint(f.Faces[0].BoundBox.Center.x,f.Faces[0].CenterOfMass.y,f.Faces[0].CenterOfMass.z) # create a point
                    else:
                        Draft.makePoint(f.Faces[0].CenterOfMass.x,f.Faces[0].CenterOfMass.y,f.Faces[0].CenterOfMass.z) # create a point
                    FreeCADGui.activeDocument().activeObject().PointColor = (red, green, blue)            
            if pad==0:
                if use_bb:
                    if edge_op == 0:
                        coordNx = f.Faces[0].BoundBox.Center.x
                        coordNy = f.Faces[0].BoundBox.Center.y
                        coordNz = f.Faces[0].BoundBox.Center.z
                        coordP  = f.Faces[0].BoundBox.Center
                    else:
                        coordNx = f.BoundBox.Center.x
                        coordNy = f.BoundBox.Center.y
                        coordNz = f.BoundBox.Center.z
                        coordP  = f.BoundBox.Center
                else:
                    if edge_op == 0:
                        coordNx = f.Faces[0].CenterOfMass.x
                        coordNy = f.Faces[0].CenterOfMass.y
                        coordNz = f.Faces[0].CenterOfMass.z
                        coordP  = f.Faces[0].CenterOfMass
                    else:
                        coordNx = f.CenterOfMass.x
                        coordNy = f.CenterOfMass.y
                        coordNz = f.CenterOfMass.z
                        coordP  = f.CenterOfMass
            else:
                if use_bb:
                    if edge_op == 0:
                        coordNx = f.Faces[0].BoundBox.Center.x
                        coordNy = f.Faces[0].BoundBox.Center.y
                        coordNz = f.Faces[0].BoundBox.Center.z
                        coordP  = f.Faces[0].BoundBox.Center
                    else:
                        coordNx = f.BoundBox.Center.x
                        coordNy = f.BoundBox.Center.y
                        coordNz = f.BoundBox.Center.z
                        coordP  = f.BoundBox.Center
                else:
                    if edge_op == 0:
                        coordNx = f.Faces[0].CenterOfMass.x
                        coordNy = f.Faces[0].CenterOfMass.y
                        coordNz = f.Faces[0].CenterOfMass.z
                        coordP  = f.Faces[0].CenterOfMass
                    else:
                        coordNx = f.CenterOfMass.x
                        coordNy = f.CenterOfMass.y
                        coordNz = f.CenterOfMass.z
                        coordP  = f.CenterOfMass
            coords.append ([coordNx,coordNy,coordNz])
            coordPs.append (coordP)
            #norm = f.Shape.Faces[0].normalAt(0,0)
            if j==0:
                if normal==1: #inverted
                    if edge_op == 0:
                        norm = f.Faces[0].normalAt(0,0)*-1
                    elif edge_op == 1:
                        norm = f.Vertex2.Point - f.Vertex1.Point
                    else:
                        norm = f.Vertex1.Point - f.Vertex2.Point
                else:
                    if edge_op == 0:
                        norm = f.Faces[0].normalAt(0,0)
                    elif edge_op == 1:
                        norm = f.Vertex2.Point - f.Vertex1.Point
                    else:
                        norm = f.Vertex2.Point - f.Vertex1.Point
                        #norm = e.normalAt(0)
            else:
                if edge_op == 0:
                    norm = f.Faces[0].normalAt(0,0)
                else:
                    norm = f.Vertex2.Point - f.Vertex1.Point
                    #norm = e.normalAt(0)
            #else:
            #    norm = f.Shape.Faces[0].normalAt(0,0)        
            say (norm)
            normals.append (norm)
            if not testing:
                FreeCAD.ActiveDocument.removeObject(fName)
            else:
                say('testing')
                #stop
            if j>0:
                pos=App.Vector(-coords[j][0]+coords[0][0],-coords[j][1]+coords[0][1],-coords[j][2]+coords[0][2])
                ## objs[j].Placement.move(pos)
                m_angle, m_angle_rad = angleBetween(normals[0],normals[j])
                say (m_angle)
                Origin = Base.Vector(0, 0, 0)
                copl=0
                if colinearVectors(normals[0], Origin, normals[j], info=1, tolerance=1e-12):
                    rot_axis = Base.Vector(0, 0, 1).cross(normals[0])
                    if rot_axis==FreeCAD.Vector (0.0, 0.0, 0.0):
                        rot_axis=Base.Vector(0, 1, 0).cross(normals[0])
                    rot_center = coordPs[j]
                    if normal==1:
                        rot_angle = 180. # + m_angleAlignFaces
                    else:
                        rot_angle=0.
                    copl=1
                    #Draft.rotate(Parent_Plane,rot_angle,rot_center,rot_axis)
                else:
                    #m_angle, m_angle_rad = angleBetween(Plane_Normal,Plane_Normal_ref)
                    rot_axis = normals[0].cross(normals[j])
                    rot_center = coordPs[j]
                    rot_angle = m_angle # + m_angleAlignFaces
                    #Draft.rotate(Parent_Plane,rot_angle,rot_center,rot_axis)
                #rot_axis = normals[0].cross(normals[j])
                #rot_center = coordPs[j]
                #rot_angle = m_angle # + m_angleAlignFaces
                sayw("axis,center,angle")
                say(rot_axis)
                say(rot_center)
                say(rot_angle)
                
                object_added=0
                if not testing2:
                    #print 'not testing2, mode  ', mode, ' rot_angle ',rot_angle
                    if rot_angle!=0: # and rot_axis!=FreeCAD.Vector (0.0, 0.0, 0.0):
                        if mode==0 or mode==2:
                            if rot_axis!=FreeCAD.Vector (0.0, 0.0, 0.0):
                                if top_level_obj[j] != 'none':
                                    o = top_level_obj[j]
                                else:
                                    o = objs[j] 
                                #sayerr(o.Name+' '+o.Label+' '+str(o.Placement)+' rotation')
                                objs_moved.append(o)
                                plc_moved.append(o.Placement)
                                object_added=1
                                ##Draft.rotate(o,-rot_angle,rot_center,rot_axis)
                                shape = Part.Shape()
                                shape.Placement = o.Placement
                                shape.rotate(DraftVecUtils.tup(rot_center), DraftVecUtils.tup(rot_axis), -rot_angle)
                                o.Placement = shape.Placement
                                rotating[j] = [rot_angle,rot_center,rot_axis]
                                say("Rotated   "+o.Label+"  : angle "+str(-rot_angle)+" center "+str(rot_center)+" axis "+str(rot_axis))
                            else:
                                rotating[j] = [0, App.Vector(0,0,0), App.Vector(0,0,0)]
                    else:
                        rotating[j] = [0, App.Vector(0,0,0), App.Vector(0,0,0)]
            ##align centers
            if j>0:
                pos=App.Vector((-coords[j][0]+coords[0][0])*cx,(-coords[j][1]+coords[0][1])*cy,(-coords[j][2]+coords[0][2])*cz)
                if mode==0 or mode==1:
                    #objs[j].Placement.move(pos)
                    if object_added==0:
                        if top_level_obj[j] != 'none':
                            o = top_level_obj[j]
                        else:
                            o = objs[j] 
                        objs_moved.append(o)
                        plc_moved.append(o.Placement)
                        #sayerr(o.Name+' '+o.Label+' '+str(o.Placement)+' centers')
                        object_added=1
                    o.Placement.move(pos)
                    moving[j] = pos
                    say("Moved   "+o.Label+"  : "+str(coordNx-coords[0][0])+" "+str(coordNy-coords[0][1])+" "+str(coordNz-coords[0][2]))
                    if mode==1:
                        rotating[j] = [0, App.Vector(0,0,0), App.Vector(0,0,0)]
                else:
                    moving[j] = App.Vector(0,0,0)

            object_added=0
            j=j+1
    
    FreeCAD.ActiveDocument.recompute()
    #for obj in objs:
    for obj in FreeCAD.ActiveDocument.Objects:
        FreeCADGui.Selection.removeSelection(obj)
    
    # except:
    #     App.Console.PrintError( "select a face"+"\n")

