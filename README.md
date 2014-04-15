[![Travis status][Travis status]][Travis project]  **STILL IN DEVELOPMENT**

# Seed Project Django
Django server for [Seed Project], based on "[AngularJS Django Rest Framework Seed]" (by [zackargyle])

Please, check the [Seed Project] for more information, compatible clients and other compatible servers.


# How to start

1. clone this project
1. Create a virtualenv: `virtualenv venv`
1. Use it: `. venv/bin/activate`
1. Download dependencies: `pip install -r requirements.txt -r requirements-dev.txt`
1. Initialize it: `fab initialize`
1. Launch the server: `fab launch`. The port as another parameter.


# License

All projects and subprojects on this meta-projects should be [MIT licensed]:

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

[AngularJS Django Rest Framework Seed]: https://github.com/zackargyle/angularjs-django-rest-framework-seed
[zackargyle]: https://github.com/zackargyle
[Seed Project]: https://github.com/seedproject/seed-project
[Travis project]: https://travis-ci.org/seedproject/seed-project-django
[Travis status]: https://travis-ci.org/seedproject/seed-project-django.svg
[MIT licensed]: http://opensource.org/licenses/MIT
