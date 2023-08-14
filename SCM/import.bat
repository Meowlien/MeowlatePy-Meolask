@ECHO OFF

SET solution=Meolask
SET proj_name=meolask
SET ver_python=3.9

SET root=%~dp0../%solution%
SET env=env-%proj_name%-py%ver_python%
SET path=%~dp0../%solution%/%env%/Scripts

SET target=\MeowkitPy\SCM\Package
