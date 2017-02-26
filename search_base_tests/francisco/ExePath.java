package tp6305.francisco;

import java.util.ArrayList;

//Make sure that your executions paths well represent the logic of the class triangle.java and could work
//with other fitness functions.

public class ExePath {

	// Operators:
	public enum Operators {
		less, equal, greater, or, and
	}
	
	int side1;
	int side2;
	int side3;
	
	ArrayList<Operators> operators = new ArrayList<Operators>();
	
	// Each condition and execution path should be clearly commented; otherwise
	// penalty points will be
	// applied.

	double fitnessValue;
	
	ExePath(int i){
		//Path 1: arguments different than 3 = illegal
		if(i == 0){
			operators.add(Operators.equal);
		}
		// Path 2: arguments equal to 3, not greater than zero = illegal
		if(i == 1){
			operators.add(Operators.greater);
			operators.add(Operators.greater);
			operators.add(Operators.greater);
		}
		//Path 3: arguments equal to 3, different than zero, side not equal, side not equal, side not equal, two side not bigger = scalene
		if(i == 2){
			operators.add(Operators.greater);
			operators.add(Operators.greater);
			operators.add(Operators.greater);
			operators.add(Operators.equal);
			operators.add(Operators.equal);
			operators.add(Operators.equal);
			operators.add(Operators.greater); //return false
			operators.add(Operators.greater); //return false
			operators.add(Operators.greater); //return false
		}
		//Path 4: arguments equal to 3, different than zero, triangle equal 0, two sides bigger = illegal
		if(i == 3){
			operators.add(Operators.greater);
			operators.add(Operators.greater);
			operators.add(Operators.greater);
			operators.add(Operators.equal);
			operators.add(Operators.equal);
			operators.add(Operators.equal);
			operators.add(Operators.greater); //return true
			operators.add(Operators.greater); //return true
			operators.add(Operators.greater); //return false
			
		}
		//Path 5: arguments equal to 3, different than zero, increment, increment, increment,triangle not
		//equal to 0, triangle bigger than 3 = equilateral
		if(i == 4){
			operators.add(Operators.greater);
			operators.add(Operators.greater);
			operators.add(Operators.greater);
			operators.add(Operators.equal);
			operators.add(Operators.equal);
			operators.add(Operators.equal);
		}
		//Path 6: arguments equal to 3, different than zero, increment, triangle not equal to 0, triangle
		//bigger than 3, (triangle equals to 1 and two sides bigger) = isosceles1
		if(i == 5){
			operators.add(Operators.greater);
			operators.add(Operators.greater);
			operators.add(Operators.greater);
			operators.add(Operators.equal);
			operators.add(Operators.equal);
			operators.add(Operators.equal); //return false
			operators.add(Operators.greater); //return true
		}
		//Path 7: arguments equal to 3, different than zero, increment, increment, triangle not equal to 0,
		//triangle bigger than 3, (triangle equals to 1 and two sides bigger) = isosceles2
		if(i == 6){
			operators.add(Operators.greater);
			operators.add(Operators.greater);
			operators.add(Operators.greater);
			operators.add(Operators.equal);
			operators.add(Operators.equal);
			operators.add(Operators.equal); //return false
			operators.add(Operators.greater); //return true 
			operators.add(Operators.greater); //return true
		}
		//Path 8: arguments equal to 3, different than zero, increment, increment, triangle not equal to 0,
		//triangle bigger than 3, (triangle equals to 1 and two sides bigger) = isosceles3
		if(i == 7){
			operators.add(Operators.greater);
			operators.add(Operators.greater);
			operators.add(Operators.greater);
			operators.add(Operators.equal);
			operators.add(Operators.equal);
			operators.add(Operators.equal); //return false
			operators.add(Operators.greater); //return true 
			operators.add(Operators.greater); //return false
			operators.add(Operators.greater); //return true
		}
		//Path 9: arguments equal to 3, different than zero, increment, increment,  triangle not equal to 0,
		//triangle bigger than 3, (triangle not equals to 1 or two sides bigger) = illegal
		if(i == 8){
			operators.add(Operators.greater);
			operators.add(Operators.greater);
			operators.add(Operators.greater);
			operators.add(Operators.equal);
			operators.add(Operators.equal);
			operators.add(Operators.equal); //return false
			operators.add(Operators.greater); //return true 
			operators.add(Operators.greater); //return true
			operators.add(Operators.greater); //return true
		}
		
	}
	
}
