"""Shared path helpers for model packages."""

import os
from pathlib import Path


def get_models_root(start: Path | None = None) -> Path:
  env_models_dir = os.getenv("LEROBOT_HUMANOID_MODELS_DIR")
  if env_models_dir:
    path = Path(env_models_dir).expanduser().resolve()
    if path.is_dir():
      return path
    raise FileNotFoundError(f"LEROBOT_HUMANOID_MODELS_DIR does not exist: {path}")

  here = (start or Path(__file__)).resolve()
  for parent in here.parents:
    path = parent / "models"
    if path.is_dir():
      return path
  raise FileNotFoundError("Could not locate 'models' directory.")


def find_repo_root(start: Path | None = None) -> Path:
  return get_models_root(start).parent


def get_model_dir(model_name: str) -> Path:
  path = get_models_root() / model_name
  if not path.is_dir():
    raise FileNotFoundError(f"Model directory not found: {path}")
  return path


def get_mjcf_dir(model_name: str) -> Path:
  path = get_model_dir(model_name) / "mjcf"
  if not path.is_dir():
    raise FileNotFoundError(f"MJCF directory not found: {path}")
  return path


def get_robot_xml(model_name: str) -> Path:
  path = get_mjcf_dir(model_name) / "robot.xml"
  if not path.is_file():
    raise FileNotFoundError(f"MJCF robot.xml not found: {path}")
  return path
