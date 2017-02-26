package tp6305.francisco;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

import tp6305.CoverageTest;

//Search Based:
public class SearchBasedTest extends CoverageTest {

	//Operators:
	public enum Operators {
	    less, equal, greater
	}
	
	int side1;
	int side2;
	int side3;
	
	//Execution paths:
	ArrayList<ExePath> myExecutionPaths = new ArrayList<ExePath>();
	
	//Copy method computeBranchCoverage from class RandomCoverageTest
	protected double computeBranchCoverage(List<String> instrumentingOutputs, String testData) {

		// new coverage calculation:
		double coverage;

		List<String> branches;
		for (String data : instrumentingOutputs) {

			if (data.contains("<trace>")) {

				//easiest way to delete part of a string:
				data = data.replace("<trace>", "");
				data = data.replace("</trace>", "");

				if (!branches.contains(data)) {
					branches.add(data);
					System.out.println(data);
				}
			}
		}

		//used for logging:
		coverage = branches.size();
		if (coverage > branches.size())
			System.out.println(coverage);

		writeBranches("branches", branches);
		// Return the relative coverage:
		return coverage / TOTAL_BRANCH_NUM;
	}
	
	//Implement Method yourname_lastname .SearchBasedTestData.generateTestData(StringBuilder, float[])
	protected void randomData(StringBuilder builder, float[] testData) {

		// Max and min parameters - hard coded:
		int max = 6;
		int min = 1;

		// For each element in testData:
		for (int i = 0; i < testData.length; i++) {

			// Call the random function:
			testData[i] = RandomCoverageTest.randInt(min, max);
			// then put them in the StringBuilder as:
			builder.append(testData[i]).append(", ");
		}

	}
	
	//Define a Method to initialize branches from class triangle.java
	protected void initiazeBranches() {

	}

	@Override
	protected void generateTestData(StringBuilder builder, float[] testData) {
		// TODO Auto-generated method stub
		
	}

	@Override
	protected double computeRACC(List<String> outputs, String testData) {
		// TODO Auto-generated method stub
		return 0;
	}
	
	protected void writeBranches(String fileName, List<String> branches) {

		try {
			PrintWriter writer = new PrintWriter(fileName+".txt", "UTF-8");

			for (String each : branches) {
				writer.println(branches + "\n");
			}

			writer.close();
		} catch (IOException e) {
		}

	}
}
