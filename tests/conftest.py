from pathlib import Path
import tomllib


def _load_test_report_paths():
    """Read [tool.test-report-paths] from pyproject.toml (single source of truth)."""
    root = Path(__file__).resolve().parent.parent
    pyproject_path = root.joinpath("pyproject.toml")
    if not pyproject_path.exists():
        raise FileNotFoundError(f"pyproject.toml not found in {root}")
   
    with open(pyproject_path, "rb") as f:
        pyproject_config = tomllib.load(f)
    return pyproject_config.get("tool", {}).get("test-report-paths")


def pytest_configure(config):
    
    paths = _load_test_report_paths()
    if paths:
        
        # JUnit XML
        junit_xml = paths.get("junit_xml", None)
        if junit_xml: config.option.xmlpath = junit_xml
        else: raise ValueError("No JUnit XML path (junit_xml) found in pyproject.toml")
        
        # JUnit HTML
        junit_html = paths.get("junit_html", None)
        if junit_html: config.option.htmlpath = junit_html

        # pytest-cov stores cov_report as a dict {report_type: dest}, not a list.
        cov_report = getattr(config.option, "cov_report", None)
        cov_report = dict() if cov_report is None or not isinstance(cov_report, dict) else cov_report
        
        # Coverage XML
        coverage_xml = paths.get("coverage_xml", None)
        if coverage_xml:
            cov_report["xml"] = coverage_xml
        else:
            raise ValueError("No Coverage XML path (coverage_xml) found in pyproject.toml")
        # Coverage HTML
        coverage_html = paths.get("coverage_html", None)
        if coverage_html:
            cov_report["html"] = coverage_html
        config.option.cov_report = cov_report
    else:
        raise ValueError("No test report paths (test-report-paths) found in pyproject.toml")


