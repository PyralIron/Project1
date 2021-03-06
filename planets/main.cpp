#include <iostream> 
#include <string> 
#include <array> 
#include <vector>
#include <initializer_list> 
#include <SDL2/SDL.h> 
#include <SDL2/SDL_opengles2.h> 
#include <fstream> 
#include <stdlib.h>
#include <cmath>
#include "vector.h" 
#include "point.h" 
#include "planet.h"
#include "camera.h"
using namespace std;

#define WINDOW_HEIGHT 1000
#define WINDOW_WIDTH 1000

bool handleevents(Camera *cam) {
	bool quit = false;
	SDL_Event event;
	while (SDL_PollEvent(&event)) {
		switch (event.type) {
		case SDL_QUIT:
			quit = true;
			break;
		case SDL_KEYDOWN:
			switch (event.key.keysym.sym) {
			case SDLK_ESCAPE:
				quit = true;
				break;
			case SDLK_w:
				cam->translate(0,0.1);
				break;
			case SDLK_s:
                                cam->translate(0,-0.1);
                                break;
			case SDLK_a:
                                cam->translate(-0.1,0);
                                break;
                        case SDLK_d:
                                cam->translate(0.1,0);
                                break;
			case SDLK_r:
				cam->rotate(0.1);
				break;
			case SDLK_t:
                                cam->rotate(-0.1);
				break;
                        }

                        break;
		}
	}
	return quit;
}

GLuint compileShader(GLenum shadertype, char* filename) {
	GLuint shader = glCreateShader(shadertype);

	fstream fin(filename, fstream::in);
	string s((istreambuf_iterator<char>(fin)), (istreambuf_iterator<char>()));
	const char * vchar = s.c_str();
	glShaderSource(shader, 1, &vchar, NULL);
	fin.close();

	glCompileShader(shader);

	GLint success = 0;
	glGetShaderiv(shader, GL_COMPILE_STATUS, &success);

	if (!success) {
		GLint logSize = 0;
		glGetShaderiv(shader, GL_INFO_LOG_LENGTH, &logSize);
		char* log = (char*)malloc(logSize);
		glGetShaderInfoLog(shader, logSize, NULL, log);
		cerr << log;
		free(log);
	}

	return shader;
}

int init(SDL_Window **window, SDL_GLContext *glcontext, GLuint *program) {
	if ( SDL_Init(SDL_INIT_EVERYTHING) != 0 )
        {
                cerr << SDL_GetError() << '\n';
                return -1;
        }
        *window = SDL_CreateWindow("", 0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, SDL_WINDOW_OPENGL);// | SDL_WINDOW_FULLSCREEN);
        if (*window == NULL)
        {
                cerr << SDL_GetError() << '\n';
                return -1;
        }
	*glcontext = SDL_GL_CreateContext(*window);
        if (*glcontext == NULL)
        {
                cerr << SDL_GetError() << '\n';
                return -1;
        }
	int version = 0;
	int version2 = 0;
	SDL_GL_GetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, &version);
	SDL_GL_GetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, &version2);
	cout << version << " " << version2 << '\n';
	glClearColor(0.0,0.0,0.0,1.0);

	GLuint vbo;
	glGenBuffers(1, &vbo);

	float vertices[] = {-1,1,
			    1,1,
 			     -1,-1,
			     1,-1};
	glEnableVertexAttribArray(0);

	glBindBuffer(GL_ARRAY_BUFFER, vbo);
	glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
	glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, 0);

	auto vshader = compileShader(GL_VERTEX_SHADER, "shader.vert");
	auto fshader = compileShader(GL_FRAGMENT_SHADER, "shader.frag");
	*program = glCreateProgram();

	glAttachShader(*program, vshader);
        glAttachShader(*program, fshader);
	glBindAttribLocation(*program, 0, "quad");
        glLinkProgram(*program);
        glDetachShader(*program, vshader);
        glDetachShader(*program, fshader);

	GLint success = 0;
        glGetProgramiv(*program, GL_LINK_STATUS, &success);

        if (!success) {
                GLint logSize = 0;
                glGetProgramiv(*program, GL_INFO_LOG_LENGTH, &logSize);
                char* log = (char*)malloc(logSize);
                glGetProgramInfoLog(*program, logSize, NULL, log);
                cerr << log;
                free(log);
        }
        glUseProgram (*program);

	//GLint apos = glGetAttribLocation(*program, "quad");
	//glBindAttribLocation(*program, 0, "quad");

	glDisable(GL_CULL_FACE);
	return 0;

}

void mm3x3(float *A, float *B, float *C) {
	C[0] = A[0]*B[0]+A[1]*B[3]+A[2]*B[6];
	C[1] = A[0]*B[1]+A[1]*B[4]+A[2]*B[7];
	C[2] = A[0]*B[2]+A[1]*B[5]+A[3]*B[8];
	C[3] = A[3]*B[0]+A[4]*B[3]+A[5]*B[6];
	C[4] = A[3]*B[1]+A[4]*B[4]+A[5]*B[7];
	C[5] = A[3]*B[2]+A[4]*B[5]+A[5]*B[8];
	C[6] = A[6]*B[0]+A[7]*B[3]+A[8]*B[6];
	C[7] = A[6]*B[1]+A[7]*B[4]+A[8]*B[7];
	C[8] = A[6]*B[2]+A[7]*B[5]+A[8]*B[8];
}
void camatrixupdate(float *cm,Camera *cam) {
	auto ca = cam->orientation;
	auto x = cam->position[0];
	auto y = cam->position[1];
	cm[0] = cos(ca)/cam->width;
	cm[1] = -sin(ca)/cam->height;
	cm[2] = -x;
	cm[3] = sin(ca)/cam->width;
	cm[4] = cos(ca)/cam->height;
	cm[5] = -y;
}

int main()
{
	SDL_Window *window = NULL;
	SDL_GLContext glcontext;
	GLuint program;
	if (init(&window, &glcontext, &program)) {
		exit(-1);
	}

	GLint upos = glGetUniformLocation(program, "pos");
        GLint ucolor = glGetUniformLocation(program, "color");
	GLint uradius = glGetUniformLocation(program, "radius");
	GLint ucamera = glGetUniformLocation(program, "camera");
	GLint udimensions = glGetUniformLocation(program, "dimensions");

	vector<Planet> planetlist = {
		Planet {"Earth", {0,-0.4}, {0.00075,0.00015}, 0.0000001, 0.1, BLUE},
		//Planet {"Sun", {0,0}, {0.001,0.0}, 0.0000001, 0.1, YELLOW},
		Planet {"Mars", {0.0,0.4}, {-0.000075,-0.00015}, 0.0000001, 0.1, RED}
		};
	vector<Vector> forcearray(planetlist.size(),{0,0});

	int win_width = 0;
	int win_height = 0;
	SDL_GetWindowSize(window, &win_width, &win_height);
	cerr << "resolution: " << win_width << " x " << win_height << '\n';
	glUniform2f(udimensions, win_width, win_height);
	glViewport(0, 0, win_width, win_height);

	Camera cam = {1,1,Point(0.0,0.0),0};

	float camatrix[9] = {1,0,0,0,1,0,0,0,1};
	camatrixupdate(camatrix,&cam);
	//float camatrix[9] = {1/cam.width,0,-cam.position[0]/cam.width,0,1/cam.height,-cam.position[1]/cam.height,0,0,1};
	glUniformMatrix3fv(ucamera, 1, 1, camatrix);
	bool quit = false;
 	while (!quit) {

		quit = handleevents(&cam);
		for (int i = 0; i < planetlist.size(); i++) {
			//cout << x.getname();
			forcearray[i] = {0,0};
			for (int j = 0; j < planetlist.size(); j++) {
				if (i != j) {
					forcearray[i] += planetlist[i].gforce(planetlist[j]);
				}
			}
		}
		for (int i = 0; i < planetlist.size(); i++) {
			auto F = forcearray[i];
			planetlist[i].velocity() = planetlist[i].getvelocity() + F/planetlist[i].getmass();
			planetlist[i].position() = planetlist[i].getposition() + planetlist[i].getvelocity();
		}
		camatrixupdate(camatrix,&cam);
		glUniformMatrix3fv(ucamera, 1, 1, camatrix);
		//SDL_FillRect(surface, NULL, BLACK);
		glClear(GL_COLOR_BUFFER_BIT);
		glEnableVertexAttribArray(0);
		//glDisableVertexAttribArray(0);
		glVertexAttrib2f(0, 0.0, 0.0);
		for (int i = 0; i < planetlist.size(); i++) {
			auto p = planetlist[i];
/*
			cout << p.getname() << ' ';
			cout << p.getposition()[0] << ' ';
			cout << p.getposition()[1] << '\n';
			cout << p.getvelocity()[0] << ' ' << p.getvelocity()[1] << '\n';

*/			Point rp = planetlist[i].getposition();
			Color color = planetlist[i].getcolor();
			long double rr = planetlist[i].getradius();
			glUniform2f(upos,rp[0],rp[1]);
			glUniform1f(uradius,rr);
			glUniform3f(ucolor,colors[color][0],colors[color][1],colors[color][2]);
			glDrawArrays(GL_TRIANGLE_STRIP, 0, 4);
		}

		SDL_GL_SwapWindow(window);
		//SDL_UpdateWindowSurface(window);
	}

	return 0;
}
