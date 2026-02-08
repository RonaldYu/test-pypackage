from pydantic import BaseModel, Field
from typing import Optional, Union
from pathlib import Path


class TestResultPath(BaseModel):
    junit_xml: Union[str, Path] = Field(..., description="The path to the JUnit XML file")
    junit_html: Optional[Union[str, Path]] = Field(None, description="The path to the JUnit HTML file")
    coverage_xml: Union[str, Path] = Field(..., description="The path to the Coverage XML file")
    coverage_html: Optional[Union[str, Path]] = Field(None, description="The path to the Coverage HTML file")

class TestPassRate(BaseModel):
    pass_rate: float = Field(..., description="The pass rate of the test")
    cov_line_rate: float = Field(..., description="The line coverage rate of the test")
    cov_branch_rate: float = Field(..., description="The branch coverage rate of the test")

class JunitResult(BaseModel):
    suites: int = Field(..., description="The number of suites")
    tests: int = Field(..., description="The number of tests")
    errors: int = Field(..., description="The number of errors")
    failures: int = Field(..., description="The number of failures")
    pass_rate: float = Field(..., description="The pass rate of the test")

class CoverageResult(BaseModel):
    line_rate: float = Field(..., description="The line coverage rate of the test")
    branch_rate: float = Field(..., description="The branch coverage rate of the test")

class TestResultSummary(BaseModel):
    test_pass_rate: TestPassRate = Field(..., description="The pass rate of the test")
    junit_result: JunitResult = Field(..., description="The result of the JUnit test")
    coverage_result: CoverageResult = Field(..., description="The result of the Coverage test")
    pass_ind: Optional[bool] = Field(None, description="True if all thresholds are met")

    def model_post_init(self, __context) -> None:
        pass_ind = (
            self.junit_result.pass_rate >= self.test_pass_rate.pass_rate
            and self.coverage_result.line_rate >= self.test_pass_rate.cov_line_rate
            and self.coverage_result.branch_rate >= self.test_pass_rate.cov_branch_rate
        )
        object.__setattr__(self, "pass_ind", pass_ind)