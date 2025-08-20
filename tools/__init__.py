import pkgutil
import importlib
import inspect
import os

tools = []
tool_functions = {}

package_dir = os.path.dirname(__file__)
for _, module_name, is_pkg in pkgutil.iter_modules([package_dir]):
    if is_pkg or module_name == "__init__":
        continue
    
    module = importlib.import_module(f"tools.{module_name}")

    if hasattr(module, "tool"):
        tools.append(module.tool)
        func_name = module.tool["function"]["name"]
        if hasattr(module, func_name) and inspect.isfunction(getattr(module, func_name)):
            tool_functions[func_name] = getattr(module, func_name)
        else:
            raise ValueError(
                f"Module {module_name} defines tool '{func_name}' but no matching function found."
            )
