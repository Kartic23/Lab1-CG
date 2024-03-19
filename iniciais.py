"""Apresenta dois polígonos"""
import OpenGL.GL as GL

from core.base import Base
from core.utils import Utils
from core.attribute import Attribute


class Example(Base):
    """ Render two shapes """
    def initialize(self):
        print("Initializing program...")
        # Initialize program #
        vs_code = """
            in vec3 position;
            void main()
            {
                gl_Position = vec4(position.x, position.y, position.z, 1.0);
            }
        """
        fs_code = """
            out vec4 fragColor;
            void main()
            {
                fragColor = vec4(0.0, 1.0, 0.0, 1.0);
            }
        """
        self.program_ref = Utils.initialize_program(vs_code, fs_code)
        # render settings #
        GL.glLineWidth(4)

        # Set up vertex array object - K #
        self.vao_K_first = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_K_first)
        position_K_first  = [[-0.75,  0.6,  0.0],
                        [-0.75,  -0.4,  0.0],
                        [-0.6,  -0.4,  0.0],
                          [-0.6,  0.6,  0.0],
                        ]
        self.vertex_count_K_first = len(position_K_first)
        position_attribute_K_first = Attribute('vec3', position_K_first)
        position_attribute_K_first.associate_variable(self.program_ref, 'position')


        self.vao_K_second = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_K_second )
        position_K_second   = [ [-0.7,  0.1,  0.0],
                        [-0.54,  0.1,  0.0],
                        [-0.15,  -0.4,  0.0],
                        [-0.28,  -0.4,  0.0],
                        ]
        self.vertex_count_K_second  = len(position_K_second )
        position_attribute_K_second  = Attribute('vec3', position_K_second )
        position_attribute_K_second .associate_variable(self.program_ref, 'position') 

        
        self.vao_K_third = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_K_third )
        position_K_third   = [[-0.15,  0.6,  0.0],
                         [-0.3,  0.6,  0.0],
                          [-0.7,  0.0,  0.0],
                          [-0.54,  0.0,  0.0],
                        ]
        self.vertex_count_K_third  = len(position_K_third )
        position_attribute_K_third  = Attribute('vec3', position_K_third )
        position_attribute_K_third .associate_variable(self.program_ref, 'position') 


        # Set up vertex array object - P #
        self.vao_pi_first = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_pi_first )
        position_pi_first   = [[0.27,  -0.39,  0.0],
                         [0.37,  -0.39,  0.0],
                          [0.44,  0.41,  0.0],
                          [0.34,  0.41,  0.0],
                        ]
        self.vertex_count_pi_first  = len(position_pi_first )
        position_attribute_pi_first  = Attribute('vec3', position_pi_first )
        position_attribute_pi_first .associate_variable(self.program_ref, 'position') 


        self.vao_pi_second = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_pi_second )
        position_pi_second   = [[0.57,  0.41,  0.0],
                         [0.69,  -0.29,  0.0],
                           [0.78,  -0.24,  0.0],
                            [0.67,  0.41,  0.0],
                        ]
        self.vertex_count_pi_second  = len(position_pi_second )
        position_attribute_pi_second  = Attribute('vec3', position_pi_second )
        position_attribute_pi_second .associate_variable(self.program_ref, 'position') 


        self.vao_pi_third = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_pi_third )
        position_pi_third   = [[0.69,  -0.29,  0.0],
                            [0.77,  -0.37,  0.0],
                          [0.87,  -0.29,  0.0],
                          [0.97,  -0.19,  0.0],
                           [0.78,  -0.24,  0.0],]
        self.vertex_count_pi_third  = len(position_pi_third )
        position_attribute_pi_third  = Attribute('vec3', position_pi_third )
        position_attribute_pi_third .associate_variable(self.program_ref, 'position') 



        self.vao_pi_fourth = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_pi_fourth )
        position_pi_fourth   = [[0.18,  0.6,  0.0],
                            [0.09,  0.27,  0.0],
                          [0.25,  0.41,  0.0]]
        self.vertex_count_pi_fourth  = len(position_pi_fourth )
        position_attribute_pi_fourth  = Attribute('vec3', position_pi_fourth )
        position_attribute_pi_fourth.associate_variable(self.program_ref, 'position') 

        self.vao_pi_fifth = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_pi_fifth )
        position_pi_fifth   = [[0.18,  0.6,  0.0],
                          [0.25,  0.41,  0.0],
                          [0.88,  0.4,  0.0],
                          [0.98,  0.57,  0.0],
                          [0.88,  0.5,  0.0]]
        self.vertex_count_pi_fifth  = len(position_pi_fifth )
        position_attribute_pi_fifth  = Attribute('vec3', position_pi_fifth)
        position_attribute_pi_fifth.associate_variable(self.program_ref, 'position') 

    def update(self):
        # Using same program to render both shapes
        GL.glUseProgram(self.program_ref)
        # Draw the K
        GL.glBindVertexArray(self.vao_K_first)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_K_first)

        GL.glBindVertexArray(self.vao_K_second)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_K_second)

        GL.glBindVertexArray(self.vao_K_third)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_K_third)

        # Draw the P
        GL.glBindVertexArray(self.vao_pi_first)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_pi_first)

        GL.glBindVertexArray(self.vao_pi_second)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_pi_second)

        GL.glBindVertexArray(self.vao_pi_third)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_pi_third)

        GL.glBindVertexArray(self.vao_pi_fourth)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_pi_fourth)

        GL.glBindVertexArray(self.vao_pi_fifth)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_pi_fifth)


# Instantiate this class and run the program
Example().run()
