#include <iostream>
#include <GLFW/glfw3.h>
#include <glad/glad.h>
using namespace std;
// GLFW is used for creating windows, handling input, and managing OpenGL contexts

struct Settings {
    int SCREEN_WIDTH;
    int SCREEN_HEIGHT;
    const char *TITLE;
};

int main() {
    int SCREEN_WIDTH = 800;
    int SCREEN_HEIGHT = 700;
    glfwInit();   // initialization of GLFW

    // glfwWindowHint is used to set configuration option that control properties of the next window
    // or OpenGL/Vulkan
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);   
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE,GLFW_OPENGL_CORE_PROFILE);

    // creating a window
    GLFWwindow* WINDOW = glfwCreateWindow(SCREEN_WIDTH, SCREEN_HEIGHT, "OpenGL windpw", NULL, NULL);

    if (WINDOW == NULL ){
        cout<<"Window not initialized"<<endl;
        glfwTerminate();
        return -1;
    }

    glfwTerminate();   // termination of GLFW
    return 0;
}