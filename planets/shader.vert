attribute vec4 quad;
uniform vec2 pos;
uniform float scale;
void main() {
	gl_Position = vec4(pos.x+scale*quad.x,pos.y+scale*quad.y,0,1);
	
}
