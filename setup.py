
from distutils.core import setup
from distutils.command.install import install

class install_with_kernel_spec(install):
    def run(self):
        install.run(self)
        from IPython.kernel.kernelspec import install_kernel_spec
        install_kernel_spec("kernel_spec", kernel_name="node", replace=True)

setup(
    py_modules=["node_kernel"],
    cmdclass= {"install" : install_with_kernel_spec }
)
