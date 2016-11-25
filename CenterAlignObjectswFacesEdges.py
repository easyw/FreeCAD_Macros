# -*- coding: utf-8 -*-

# evolution of Macro_CenterFace
# and some part of Macro WorkFeature
#
# center objs faces/closed_edges to first obj face/closed_edge
#
 
__title__   = "Center Faces of Parts"
__author__  = "maurice"
__url__     = "kicad stepup"
__version__ = "0.32"
__date__    = "11.2016"

# * (C) Maurice easyw-fc 2016
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Library General Public License (LGPL)   *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *

## done case: invert normal and standard when already aligned planes
## done works for Bodys on FC 0.17

import FreeCAD, FreeCADGui, Draft, Part, DraftTools
from FreeCAD import Base

# Form implementation generated from reading ui file 'C:\Cad\Progetti_K\3D-FreeCad-tools\CenterAlignObjectswFacesEdges.ui'
#
# Created: Wed Nov 23 23:17:52 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CenterAlignObjectsFacesEdges(object):
    def setupUi(self, CenterAlignObjectsFacesEdges):
        CenterAlignObjectsFacesEdges.setObjectName("CenterAlignObjectsFacesEdges")
        CenterAlignObjectsFacesEdges.setWindowModality(QtCore.Qt.NonModal)
        CenterAlignObjectsFacesEdges.resize(367, 351)
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
        self.rb_bb.setGeometry(QtCore.QRect(11, 20, 161, 20))
        self.rb_bb.setChecked(True)
        self.rb_bb.setObjectName("rb_bb")
        self.rb_mass = QtGui.QRadioButton(self.groupBox)
        self.rb_mass.setGeometry(QtCore.QRect(200, 20, 121, 20))
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
        self.rb_centers_planes.setGeometry(QtCore.QRect(20, 80, 261, 20))
        self.rb_centers_planes.setChecked(True)
        self.rb_centers_planes.setObjectName("rb_centers_planes")
        self.cb_x = QtGui.QCheckBox(self.groupBox_2)
        self.cb_x.setGeometry(QtCore.QRect(290, 40, 41, 20))
        self.cb_x.setChecked(True)
        self.cb_x.setObjectName("cb_x")
        self.cb_y = QtGui.QCheckBox(self.groupBox_2)
        self.cb_y.setGeometry(QtCore.QRect(290, 60, 41, 20))
        self.cb_y.setChecked(True)
        self.cb_y.setObjectName("cb_y")
        self.cb_z = QtGui.QCheckBox(self.groupBox_2)
        self.cb_z.setGeometry(QtCore.QRect(290, 80, 41, 20))
        self.cb_z.setChecked(True)
        self.cb_z.setObjectName("cb_z")
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(270, 20, 61, 16))
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
        self.verticalLayout_3.addLayout(self.hLayout1)
        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(CenterAlignObjectsFacesEdges)
        QtCore.QMetaObject.connectSlotsByName(CenterAlignObjectsFacesEdges)

    def retranslateUi(self, CenterAlignObjectsFacesEdges):
        CenterAlignObjectsFacesEdges.setWindowTitle(QtGui.QApplication.translate("CenterAlignObjectsFacesEdges", "Center Align Faces/Edges", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_info.setText(QtGui.QApplication.translate("CenterAlignObjectsFacesEdges", "Select multiple face(s) or closed Edges and click Align", None, QtGui.QApplication.UnicodeUTF8))
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
        self.label.setText(QtGui.QApplication.translate("CenterAlignObjectsFacesEdges", "First Face/Edge is the Reference for alignment", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAlign.setText(QtGui.QApplication.translate("CenterAlignObjectsFacesEdges", "Align", None, QtGui.QApplication.UnicodeUTF8))


### ------------------------------------------------------------------------------------ ###
### ---------code to be inserted and remove from new generation------------------------- ###
### ------------------------------------------------------------------------------------ ###
        self.btnAlign.clicked.connect(self.onAlign)
        
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

def say(msg):
    FreeCAD.Console.PrintMessage(msg)
    FreeCAD.Console.PrintMessage('\n')

def sayw(msg):
    FreeCAD.Console.PrintWarning(msg)
    FreeCAD.Console.PrintWarning('\n')
    
def singleInstance():
    app = QtGui.qApp

    for i in app.topLevelWidgets():
        if i.objectName() == "CenterAlignObjectsFacesEdges":
            i.deleteLater()
        else:
            pass
#    t=FreeCADGui.getMainWindow()
#    dw=t.findChildren(QtGui.QDockWidget)
#    #print str(dw)
#    for i in dw:
#        print str(i.objectName())
#        if str(i.objectName()) == "CenterAlignObjectsFacesEdges": #"kicad StepUp 3D tools":
#            i.deleteLater()
#        else:
#            pass

## assigning DisplayModeBody to Tip to attach Facebinder to Body
doc=FreeCAD.ActiveDocument
bodys=[]
bo_name = ""
for o in doc.Objects:
    #print o.Name
    if 'Body' in o.Name and 'Origin' not in o.Name:
        bodys.append(o)
        FreeCADGui.ActiveDocument.getObject(o.Name).DisplayModeBody = u"Tip"    

singleInstance()

CenterAlignObjectsFacesEdges = QtGui.QWidget()
ui = Ui_CenterAlignObjectsFacesEdges()
ui.setupUi(CenterAlignObjectsFacesEdges)
#CenterAlignObjectsFacesEdges.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
CenterAlignObjectsFacesEdges.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowSystemMenuHint);
#self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
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
CenterAlignObjectsFacesEdges.move(10,100)
## to do:
## ok single instance
## - always on top
## - no maximize
### ------------------------------------------------------------------------------------ ###
### ---------code to be inserted and remove from new generation------------------------- ###
### ------------------------------------------------------------------------------------ ###

def Align(normal,type,mode,cx,cy,cz):
    #cx = 1  # center x -> 1  
    #cy = 1  # center y -> 1 
    #cz = 1  # center z -> 1 
    say(str(cx)+str(cy)+str(cz))
    create_points=False
    use_bb = True #align center based on bounding boxes or center of mass
    if type==1:
        use_bb = False #align center based on bounding boxes or center of mass

    #def say(msg):
    #    FreeCAD.Console.PrintMessage(msg)
    #    FreeCAD.Console.PrintMessage('\n')
    #
    #def sayw(msg):
    #    FreeCAD.Console.PrintWarning(msg)
    #    FreeCAD.Console.PrintWarning('\n')
    
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
    
    sel = FreeCADGui.Selection.getSelection()
    selEx = FreeCADGui.Selection.getSelectionEx()
    say("number of objects: "+ str(len(selEx)))
    objs = [selobj.Object for selobj in selEx]
    
    say(objs)
    coords = []
    normals = []
    coordPs = []
    sEdge = []
    j = 0
    # .BoundBox.Center
    #align faces
    if (len(selEx) > 1) and (len(selEx)==len(sel)):
        #s = obj.Shape
        for fc in selEx:
            say ("j= "+str(j))
            say("len selEx "+str(len(selEx)))
            s=fc
            #selectedEdge = FreeCADGui.Selection.getSelectionEx()[j].SubObjects[0] # select one element SubObjects    
            selectedEdge = selEx[j].SubObjects[0] # select one element SubObjects    
            sEdge.append(selectedEdge)
            pad=0
            if str(fc.SubObjects[0])[1:5] != "Face":
                wire = Part.Wire(selectedEdge)
                fw = Part.Face(wire)
                #Part.show(fw)
                f=FreeCAD.ActiveDocument.addObject("Part::Feature","Facebinder")
                f.Shape=fw 
                pad=1
                #FreeCAD.ActiveDocument.recompute()
                say("Label : "+ str(sel[j].Label))     # extract the Label
                say("Name  : "+ str(sel[j].Name))     # extract the Name
                say( "Center Face Binder "+str(0)+" "+str(FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].CenterOfMass)) # Vector center mass to face
                say( "Center Face Binder bb "+str(0)+" "+str(FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].BoundBox.Center)) # Vector center mass to face
            else:
                pad=0
                f=Draft.makeFacebinder(s)
                say("Label : "+ str(sel[j].Label))     # extract the Label
                say("Name  : "+ str(sel[j].Name))     # extract the Name
                say( "Center Face Binder "+str(0)+" "+str(f.Shape.Faces[0].CenterOfMass)) # Vector center mass to face
                say( "Center Face Binder bb "+str(0)+" "+str(f.Shape.Faces[0].BoundBox.Center)) # Vector center mass to face
            # LineColor
            red   = 1.0  # 1 = 255
            green = 0.0  #
            blue  = 0.0  #
            if create_points:
                if pad==0:
                    if use_bb:
                        Draft.makePoint(f.Shape.Faces[0].BoundBox.Center.x,f.Shape.Faces[0].BoundBox.Center.y,f.Shape.Faces[0].BoundBox.Center.z) # create a point
                    else:
                        Draft.makePoint(f.Shape.Faces[0].CenterOfMass.x,f.Shape.Faces[0].CenterOfMass.y,f.Shape.Faces[0].CenterOfMass.z) # create a point
                    FreeCADGui.activeDocument().activeObject().PointColor = (red, green, blue)
                else:
                    if use_bb:
                        Draft.makePoint(FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].BoundBox.Center.x,FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].CenterOfMass.y,FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].CenterOfMass.z) # create a point
                    else:
                        Draft.makePoint(FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].CenterOfMass.x,FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].CenterOfMass.y,FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].CenterOfMass.z) # create a point
                    FreeCADGui.activeDocument().activeObject().PointColor = (red, green, blue)            
            if pad==0:
                if use_bb:
                    coordNx = f.Shape.Faces[0].BoundBox.Center.x
                    coordNy = f.Shape.Faces[0].BoundBox.Center.y
                    coordNz = f.Shape.Faces[0].BoundBox.Center.z
                    coordP  = f.Shape.Faces[0].BoundBox.Center
                else:
                    coordNx = f.Shape.Faces[0].CenterOfMass.x
                    coordNy = f.Shape.Faces[0].CenterOfMass.y
                    coordNz = f.Shape.Faces[0].CenterOfMass.z
                    coordP  = f.Shape.Faces[0].CenterOfMass
            else:
                if use_bb:
                    coordNx = FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].BoundBox.Center.x
                    coordNy = FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].BoundBox.Center.y
                    coordNz = FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].BoundBox.Center.z
                    coordP  = FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].BoundBox.Center
                else:
                    coordNx = FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].CenterOfMass.x
                    coordNy = FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].CenterOfMass.y
                    coordNz = FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].CenterOfMass.z
                    coordP  = FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].CenterOfMass
            coords.append ([coordNx,coordNy,coordNz])
            coordPs.append (coordP)
            #norm = f.Shape.Faces[0].normalAt(0,0)
            if j==0:
                if normal==1:
                    norm = f.Shape.Faces[0].normalAt(0,0)*-1
                else:
                    norm = f.Shape.Faces[0].normalAt(0,0)
            else:
                norm = f.Shape.Faces[0].normalAt(0,0)
            #else:
            #    norm = f.Shape.Faces[0].normalAt(0,0)        
            say (norm)
            normals.append (norm)
            FreeCAD.ActiveDocument.removeObject(f.Name)
            if j>0:
                pos=App.Vector(-coords[j][0]+coords[0][0],-coords[j][1]+coords[0][1],-coords[j][2]+coords[0][2])
                ## objs[j].Placement.move(pos)
                m_angle, m_angle_rad = angleBetween(normals[0],normals[j])
                say (m_angle)
                Origin = Base.Vector(0, 0, 0)
                copl=0
                #rot_angle = m_angle 
                rot_axis = normals[0].cross(normals[j])
                rot_center = coordPs[j]
                rot_angle = m_angle # + m_angleAlignFaces
                if rot_axis==FreeCAD.Vector (0.0, 0.0, 0.0):
                    if colinearVectors(normals[0], Origin, normals[j], info=1, tolerance=1e-12):
                        rot_axis = Base.Vector(0, 0, 1).cross(normals[0])
                        if rot_axis==FreeCAD.Vector (0.0, 0.0, 0.0):
                            rot_axis=Base.Vector(0, 1, 0).cross(normals[0])
                        rot_center = coordPs[j]
                        if normal==1:
                            #if rot_angle!=180.:
                            rot_angle = 180. # + m_angleAlignFaces
                            #else:
                            #    rot_angle=0.
                        else:
                            #if rot_angle!=0.:
                            rot_angle=0.
                            #else:
                            #    rot_angle=180.
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
                say("axis,center,angle")
                say(rot_axis)
                say(rot_center)
                say(rot_angle)
                if rot_angle!=0: # and rot_axis!=FreeCAD.Vector (0.0, 0.0, 0.0):
                    if mode==0 or mode==2:
                        if rot_axis!=FreeCAD.Vector (0.0, 0.0, 0.0):
                            Draft.rotate(objs[j],-rot_angle,rot_center,rot_axis)
                            say("Rotated     : angle "+str(-rot_angle)+" center "+str(rot_center)+" axis "+str(rot_axis))
            j=j+1
    
    coords = []
    normals = []
    coordPs = []
    j = 0
    
    #align centers
    if (len(selEx) >= 1) and (len(selEx)==len(sel)):
        #s = obj.Shape
        for fc in selEx:
            s=fc
            print j
            #selectedEdge = FreeCADGui.Selection.getSelectionEx()[j].SubObjects[0] # select one element SubObjects    
            selectedEdge = sEdge[j] # select one element SubObjects    
            pad=0
            if str(fc.SubObjects[0])[1:5] != "Face":
                wire = Part.Wire(selectedEdge)
                fw = Part.Face(wire)
                #Part.show(fw)
                f=FreeCAD.ActiveDocument.addObject("Part::Feature","Facebinder")
                f.Shape=fw 
                pad=1
                #FreeCAD.ActiveDocument.recompute()
            else:
                pad=0
                f=Draft.makeFacebinder(s)
            say("Label : "+ str(sel[j].Label))     # extract the Label
            say("Name  : "+ str(sel[j].Name))     # extract the Name
            say( "Center Face Binder "+str(0)+" "+str(f.Shape.Faces[0].CenterOfMass)) # Vector center mass to face
            say( "Center Face Binder bb "+str(0)+" "+str(f.Shape.Faces[0].BoundBox.Center)) # Vector center mass to face
            # LineColor
            red   = 1.0  # 1 = 255
            green = 0.0  #
            blue  = 0.0  #
            if create_points:
                if pad==0:
                    Draft.makePoint(f.Shape.Faces[0].CenterOfMass.x,f.Shape.Faces[0].CenterOfMass.y,f.Shape.Faces[0].CenterOfMass.z) # create a point
                    FreeCADGui.activeDocument().activeObject().PointColor = (red, green, blue)
                else:
                    Draft.makePoint(FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].CenterOfMass.x,FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].CenterOfMass.y,FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].CenterOfMass.z) # create a point
                    FreeCADGui.activeDocument().activeObject().PointColor = (red, green, blue)            
            if pad==0:
                if use_bb:
                    coordNx = f.Shape.Faces[0].BoundBox.Center.x
                    coordNy = f.Shape.Faces[0].BoundBox.Center.y
                    coordNz = f.Shape.Faces[0].BoundBox.Center.z
                    coordP  = f.Shape.Faces[0].BoundBox.Center
                else:
                    coordNx = f.Shape.Faces[0].CenterOfMass.x
                    coordNy = f.Shape.Faces[0].CenterOfMass.y
                    coordNz = f.Shape.Faces[0].CenterOfMass.z
                    coordP  = f.Shape.Faces[0].CenterOfMass
                norm = f.Shape.Faces[0].normalAt(0,0)
            else:
                if use_bb:
                    coordNx = FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].BoundBox.Center.x
                    coordNy = FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].BoundBox.Center.y
                    coordNz = FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].BoundBox.Center.z
                    coordP  = FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].BoundBox.Center
                else:
                    coordNx = FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].CenterOfMass.x
                    coordNy = FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].CenterOfMass.y
                    coordNz = FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].CenterOfMass.z
                    coordP  = FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].CenterOfMass
                norm    = FreeCAD.ActiveDocument.getObject(f.Name).Shape.Faces[0].normalAt(0,0)
            coords.append ([coordNx,coordNy,coordNz])
            coordPs.append (coordP)
            say (norm)
            normals.append (norm)
            FreeCAD.ActiveDocument.removeObject(f.Name)
            if j>0:
                pos=App.Vector((-coords[j][0]+coords[0][0])*cx,(-coords[j][1]+coords[0][1])*cy,(-coords[j][2]+coords[0][2])*cz)
                if mode==0 or mode==1:
                    objs[j].Placement.move(pos)
                    say("Moved     : "+str(coordNx-coords[0][0])+" "+str(coordNy-coords[0][1])+" "+str(coordNz-coords[0][2]))
            j=j+1
    
    for obj in objs:
        FreeCADGui.Selection.removeSelection(obj)
    
    # except:
    #     App.Console.PrintError( "select a face"+"\n")

