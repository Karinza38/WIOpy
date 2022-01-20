from distutils.core import setup
import io
import os.path as op

def read(*parts, **kwargs):
    encoding = kwargs.pop('encoding', 'utf-8')
    filepath = op.join(op.dirname(__file__), *parts)
    return io.open(filepath, encoding=encoding).read()

setup(
  name = 'WIOpy',
  packages = ['WIOpy'],
  version = '0.0.1',
  license='MIT',
  
  description = 'Walmart IO API python wrapper',
  long_description=read('README.md'),
  long_description_content_type='text/markdown',

  author = 'CoderJosh',
  author_email = '74162303+CoderJoshDK@users.noreply.github.com',
  url = 'https://github.com/CoderJoshDK/WIOpy',
  download_url = 'https://github.com/CoderJoshDK/WIOpy/archive/refs/tags/v_001-alpha.tar.gz',
  keywords = ['API', 'Wrapper', 'Python', 'Walmart', 'Affiliate', 'WalmartIO'],
  install_requires=[
          'requests',
          'pycryptodome',
      ],
  
  classifiers=[
      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
      'Development Status :: 3 - Alpha',      

      'Intended Audience :: Developers',      # Define that your audience are developers
      'Topic :: Software Development :: Build Tools',
      
      'License :: OSI Approved :: MIT License',
  
      'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Programming Language :: Python :: 3.8',
      'Programming Language :: Python :: 3.9',
  ],
)
