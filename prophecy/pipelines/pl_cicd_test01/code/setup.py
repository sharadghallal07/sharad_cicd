from setuptools import setup, find_packages
setup(
    name = 'pl_cicd_test01',
    version = '1.0',
    packages = find_packages(include = ('pl_cicd_test01*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.9.9'],
    entry_points = {
'console_scripts' : [
'main = pl_cicd_test01.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
