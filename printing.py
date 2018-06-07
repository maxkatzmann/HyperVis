# This program visualizes hyperbolic circles using the native representation.
# Copyright (C) 2018    Maximilian Katzmann
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
#
# You can contact the author via email: max.katzmann@gmail.com

import euclidean_coordinates
import native_coordinates
import math
import drawing

class printer:

    def __init__(self, drawer):
        self.drawer = drawer

    def print_ipe(self, items, edges, selected_nodes):

        print("<?xml version=\"1.0\"?>\n" +\
              "<!DOCTYPE ipe SYSTEM \"ipe.dtd\">\n" +\
              "<ipe version=\"70206\" creator=\"Ipe 7.2.7\">\n" +\
              "<info created=\"D:20170719160807\" modified=\"D:20170719160807\"/>\n" +\
              "<ipestyle name=\"basic\">\n" +\
              "</ipestyle>\n" +\
              "<page>\n" +\
              "<layer name=\"alpha\"/>\n" +\
              "<view layers=\"alpha\" active=\"alpha\"/>\n")

        self.drawer.draw_with_functions(items,
                                        edges,
                                        selected_nodes,
                                        self.print_ipe_line,
                                        self.print_ipe_circle)

        print("</page>\n" +\
              "</ipe>")

    def print_ipe_line(self, coord1, coord2, color):
        print("<path stroke=\"" + str(color) + "\">\n" +\
              str(coord1.x) + " " + str(coord1.y) + " m\n" +\
              str(coord2.x) + " " + str(coord2.y) + " l\n" +\
              "</path>")

    def print_ipe_circle(self, center, radius, start_angle, end_angle, is_clockwise, fill_color, border_color, width):
        if len(fill_color) > 0:
            print("<path stroke=\"" + str(fill_color) + "\" fill=\"" + str(fill_color) + "\"> " + str(radius) + " 0 0 " + str(radius) + " " + str(center.x) + " " + str(center.y) + " e </path>")
        else:
            print("<path stroke=\"" + str(border_color) + "\"> " + str(radius) + " 0 0 " + str(radius) + " " + str(center.x) + " " + str(center.y) + " e </path>")

    ### SVG ###

    def print_svg(self, items, edges, selected_nodes):
        print("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE svg PUBLIC " +\
              "\"-//W3C//DTD SVG 1.1//EN\" " +\
              "\"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\n\n<svg " +\
              "xmlns=\"http://www.w3.org/2000/svg\"\nxmlns:xlink=\"http://" +\
              "www.w3.org/1999/xlink\" " +\
              "xmlns:ev=\"http://www.w3.org/2001/xml-events\"\nversion=\"1.1\" " +\
              "baseProfile=\"full\"\nwidth=\"" + str(self.drawer.canvas.winfo_width()) + "\" height=\"" + str(self.drawer.canvas.winfo_height()) + "\">\n\n")

        self.drawer.draw_with_functions(items,
                                        edges,
                                        selected_nodes,
                                        self.print_svg_line,
                                        self.print_svg_circle)

        print("\n</svg>\n")

    def print_svg_line(self, coord1, coord2, color):
        print("<line x1=\"" + str(coord1.x) + "\" y1=\"" + str(coord1.y) + "\" x2=\"" + str(coord2.x) + "\" y2=\"" + str(coord2.y) + "\" stroke=\"" + str(color) + "\" stroke-width=\"1.0\" opacity=\"1.0\"/>\n")

    def print_svg_circle(self, center, radius, start_angle, end_angle, is_clockwise, fill_color, border_color, width):
        if len(fill_color) > 0:
            print("<circle cx=\"" + str(center.x) + "\" cy=\"" + str(center.y) + "\" r=\"" + str(radius) + "\" fill=\"" + str(fill_color) + "\" stroke=\"" + str(fill_color) + "\" stroke-width=\"" + str(width) + "\"/>\n")
        else:
            print("<circle cx=\"" + str(center.x) + "\" cy=\"" + str(center.y) + "\" r=\"" + str(radius) + "\" fill=\"clear\" stroke=\"" + str(border_color) + "\" stroke-width=\"" + str(width) + "/>\n")