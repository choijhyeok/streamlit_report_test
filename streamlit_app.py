import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe
import streamlit.components.v1 as components

components.html("""

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">
  <link rel="icon" type="image/png" href="images/favicon-32x32.png" sizes="32x32" />
  <link rel="icon" type="image/png" href="images/favicon-16x16.png" sizes="16x16" />
  <title>Travel</title>
  <!--stylesheet-->
  <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,700,900" rel="stylesheet">
  <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" type="text/css">
  <link href="styles/styles.css" rel="stylesheet" type="text/css">
  <link href="styles/custom-responsive-styles.css" rel="stylesheet" type="text/css">
  <!--scripts-->
  <script type="text/javascript" src="scripts/jquery-3.2.1.min.js"></script>
  <script type="text/javascript" src="scripts/all-plugins.js"></script>
  <script type="text/javascript" src="scripts/plugins-activate.js"></script>
</head>

<body id="page-top">
  <!-- Navigation -->
  <div class="logo">
    <i class="fa fa-plane" aria-hidden="true"><span>Travel</span></i>
  </div>

  <nav id="sidebar-wrapper">
    <ul class="sidebar-nav">
      <li class="sidebar-brand">
        <a class="smooth-scroll" href="#Header"></a>
      </li>
      <li class="sidebar-nav-item">
        <a class="smooth-scroll" href="#page-top">Home</a>
      </li>
      <li class="sidebar-nav-item">
        <a class="smooth-scroll" href="#About">About</a>
      </li>
      <li class="sidebar-nav-item">
        <a class="smooth-scroll" href="#Services">Services</a>
      </li>
      <li class="sidebar-nav-item">
        <a class="smooth-scroll" href="#Portfolio">Portfolio</a>
      </li>
      <li class="sidebar-nav-item">
        <a class="smooth-scroll" href="#Testimonials">Testimonials</a>
      </li>
      <li class="sidebar-nav-item">
        <a class="smooth-scroll" href="#Contact">Contact</a>
      </li>
    </ul>
  </nav>
  <!-- Header Starts -->
  <section id="Banner" class="content-section" style="height: 300px;">
    <div class="container content-wrap text-center">
      <h3 style="color: black;">최재혁님의 여행스타그램 발자취</h3>
      <p>
          <em>A Bootstrap Theme to start building a new landing page</em>
      </p>
      <a class="btn btn-primary btn-xl smooth-scroll" href="#About">Find Out More</a>
    </div>
    <div class="overlay"></div>
  </section>
  <!-- Header Ends -->
  <!-- About Us Starts -->
  <section id="About" class="content-section">
    <div class="container text-center">
      <div class="row">
        <div class="col-lg-12">
          <div class="block-heading">
            <h2>About Us</h2>
          </div>
          <p class="lead">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.</p>
        </div>
      </div>
    </div>
  </section>
  <!-- About Us Starts -->
  <section id="Services" class="content-section text-center">
    <div class="container">
      <div class="block-heading">
        <h2>What We Offer</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
      </div>
      <div class="row">
        <div class="col-md-3 col-sm-6">
          <div class="service-box">
            <div class="service-icon yellow">
              <div class="front-content">
                <i class="fa fa-globe" aria-hidden="true"></i>
                <h3>Family Travel</h3>
              </div>
            </div>
            <div class="service-content">
              <h3>Family Travel</h3>
              <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text</p>
            </div>
          </div>
        </div>
        <div class="col-md-3 col-sm-6">
          <div class="service-box">
            <div class="service-icon orange">
              <div class="front-content">
                <i class="fa fa-suitcase"></i>
                <h3>Business Travel</h3>
              </div>
            </div>
            <div class="service-content">
              <h3>Business Travel</h3>
              <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text</p>
            </div>
          </div>
        </div>
        <div class="col-md-3 col-sm-6">
          <div class="service-box ">
            <div class="service-icon red">
              <div class="front-content">
                <i class="fa fa-male" aria-hidden="true"></i>
                <h3>Solo Travel</h3>
              </div>
            </div>
            <div class="service-content">
              <h3>Solo Travel</h3>
              <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text</p>
            </div>
          </div>
        </div>
        <div class="col-md-3 col-sm-6">
          <div class="service-box">
            <div class="service-icon grey">
              <div class="front-content">
                <i class="fa fa-users"></i>
                <h3>Camping</h3>
              </div>
            </div>
            <div class="service-content">
              <h3>Camping</h3>
              <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <section class="content-section text-center" id="Portfolio">
    <div class="container">
      <div class="block-heading">
        <h2>Portfolio</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
      </div>
      <div class="portfolio-wrapper clearfix">
        <a class="each-portfolio" data-fancybox="gallery" href="images/p-two.jpeg">
          <div class="content hover-cont-wrap">
            <div class="content-overlay"></div>
            <img class="content-image" src="images/p-two.jpeg">
            <div class="content-details fadeIn-bottom">
              <h5 class="p-title">Title</h5>
              <p class="p-desc">Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
              <span class="zoom"><i class="fa fa-search-plus"></i></span>
            </div>
          </div>
        </a>
        <a class="each-portfolio" data-fancybox="gallery" href="images/p-three.jpeg">
          <div class="content hover-cont-wrap">
            <div class="content-overlay"></div>
            <img class="content-image" src="images/p-three.jpeg">
            <div class="content-details fadeIn-bottom">
              <h5 class="p-title">Title</h5>
              <p class="p-desc">Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
              <span class="zoom"><i class="fa fa-search-plus"></i></span>
            </div>
          </div>
        </a>
        <a class="each-portfolio" data-fancybox="gallery" href="images/p-four.jpeg">
          <div class="content hover-cont-wrap">
            <div class="content-overlay"></div>
            <img class="content-image" src="images/p-four.jpeg">
            <div class="content-details fadeIn-bottom">
              <h5 class="p-title">Title</h5>
              <p class="p-desc">Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
              <span class="zoom"><i class="fa fa-search-plus"></i></span>
            </div>
          </div>
        </a>
        <a class="each-portfolio" data-fancybox="gallery" href="images/p-five.jpeg">
          <div class="content hover-cont-wrap">
            <div class="content-overlay"></div>
            <img class="content-image" src="images/p-five.jpeg">
            <div class="content-details fadeIn-bottom">
              <h5 class="p-title">Title</h5>
              <p class="p-desc">Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
              <span class="zoom"><i class="fa fa-search-plus"></i></span>
            </div>
          </div>
        </a>
        <a class="each-portfolio" data-fancybox="gallery" href="images/p-six.jpeg">
          <div class="content hover-cont-wrap">
            <div class="content-overlay"></div>
            <img class="content-image" src="images/p-six.jpeg">
            <div class="content-details fadeIn-bottom">
              <h5 class="p-title">Title</h5>
              <p class="p-desc">Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
              <span class="zoom"><i class="fa fa-search-plus"></i></span>
            </div>
          </div>
        </a>
        <a class="each-portfolio" data-fancybox="gallery" href="images/p-three.jpeg">
          <div class="content hover-cont-wrap">
            <div class="content-overlay"></div>
            <img class="content-image" src="images/p-three.jpeg">
            <div class="content-details fadeIn-bottom">
              <h5 class="p-title">Title</h5>
              <p class="p-desc">Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
              <span class="zoom"><i class="fa fa-search-plus"></i></span>
            </div>
          </div>
        </a>
      </div>
    </div>
  </section>
  <!-- TESTIMONIALS -->
  <section id="Testimonials" class="content-section">
    <div class="container">
      <div class="row">
        <div class="col-sm-12">
          <div class="block-heading">
            <h2>Testimonials</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
          </div>
          <div id="customers-testimonials" class="owl-carousel">
            <div class="item">
              <div class="shadow-effect">
                <img class="img-circle" src="images/sarah.jpg" alt="">
                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s</p>
              </div>
              <div class="testimonial-name">Sarah Jenks</div>
            </div>
            <div class="item">
              <div class="shadow-effect">
                <img class="img-circle" src="images/tangelia.jpg" alt="">
                <p>Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old</p>
              </div>
              <div class="testimonial-name">Tangelia Ekhoff</div>
            </div>
            <div class="item">
              <div class="shadow-effect">
                <img class="img-circle" src="images/john-doe.jpg" alt="">
                <p>There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. </p>
              </div>
              <div class="testimonial-name">John Doe</div>
            </div>
            <div class="item">
              <div class="shadow-effect">
                <img class="img-circle" src="images/amy.jpg" alt="">
                <p>All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words</p>
              </div>
              <div class="testimonial-name">Amy Tan</div>
            </div>
            <div class="item">
              <div class="shadow-effect">
                <img class="img-circle" src="images/daniel.jpg" alt="">
                <p>Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy.</p>
              </div>
              <div class="testimonial-name">Daniel Felsted</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- END OF TESTIMONIALS -->
  <section id="Contact" class="content-section">
    <div class="container">
      <div class="block-heading">
        <h2>Contact Us</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
      </div>
      <div class="row">
        <div class="col-sm-12 col-md-6 col-lg-6">
          <div class="contact-wrapper">
            <div class="address-block border-bottom">
              <h3 class="add-title">Headquaters</h3>
              <div class="c-detail">
                <span class="c-icon"><i class="fa fa-map-marker" aria-hidden="true"></i></span><span class="c-info">&nbsp;35 Street - Cheyenne, CO 80810</span>
              </div>
              <div class="c-detail">
                <span class="c-icon"><i class="fa fa-phone" aria-hidden="true"></i></span><span class="c-info">+123 4567 898</span>
              </div>
              <div class="c-detail">
                <span class="c-icon"><i class="fa fa-envelope" aria-hidden="true"></i></span><span class="c-info">email@yourdomain.com</span>
              </div>
            </div>
            <div class="address-block">
              <h3 class="add-title">Branch</h3>
              <div class="c-detail">
                <span class="c-icon"><i class="fa fa-map-marker" aria-hidden="true"></i></span><span class="c-info">&nbsp;98 Berry - Cheyenne, CO 80810</span>
              </div>
              <div class="c-detail">
                <span class="c-icon"><i class="fa fa-phone" aria-hidden="true"></i></span><span class="c-info">+123 4567 8987</span>
              </div>
              <div class="c-detail">
                <span class="c-icon"><i class="fa fa-envelope" aria-hidden="true"></i></span><span class="c-info">email@yourdomain.com</span>
              </div>
            </div>
          </div>
        </div>
        <div class="col-sm-12 col-md-6 col-lg-6">
          <div class="form-wrap">
            <form action="javascript:void(0)" method="post">
              <div class="fname floating-label">
                <input type="text" class="floating-input" name="full name" />
                <label for="title">First Name</label>
              </div>
              <div class="fname floating-label">
                <input type="text" class="floating-input" name="full name" />
                <label for="title">Last Name</label>
              </div>
              <div class="email floating-label">
                <input type="email" class="floating-input" name="email" />
                <label for="email">Email</label>
              </div>
              <div class="contact floating-label">
                <input type="tel" class="floating-input" name="contact" />
                <label for="email">Mobile</label>
              </div>
              <div class="company floating-label">
                <textarea type="text" class="floating-input" name="company" /></textarea>
                <label for="email">Message</label>
              </div>
              <div class="submit-btn">
                <button type="submit">Submit</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>
  <footer class="footer text-center">
    <div class="container">
      <ul class="list-inline">
        <li class="list-inline-item">
          <a class="social-link rounded-circle text-white mr-3" href="javascript:void(0)">
              <i class="fa fa-facebook" aria-hidden="true"></i>
            </a>
        </li>
        <li class="list-inline-item">
          <a class="social-link rounded-circle text-white mr-3" href="javascript:void(0)">
              <i class="fa fa-twitter" aria-hidden="true"></i>
            </a>
        </li>
        <li class="list-inline-item">
          <a class="social-link rounded-circle text-white" href="javascript:void(0)">
              <i class="fa fa-linkedin" aria-hidden="true"></i>
            </a>
        </li>
      </ul>
      <p class="text-muted small mb-0">Copyright © Your Website 2018</p>
      <p class="text-muted small mb-0">Designed by <a href="https://www.position2.com/" target="_balnk">Position2</p>
    </div>
  </footer>
</body>

</html>

""",
height=600
)
                
# st.set_page_config(layout="centered", page_icon="🎓", page_title="Diploma Generator")
# st.title("🎓 Diploma PDF Generator")

# st.write(
#     "This app shows you how you can use Streamlit to make a PDF generator app in just a few lines of code!"
# )

# left, right = st.columns(2)

# right.write("Here's the template we'll be using:")

# right.image("template.png", width=300)

# env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
# template = env.get_template("template.html")


# left.write("Fill in the data:")
# form = left.form("template_form")
# student = form.text_input("Student name")
# course = form.selectbox(
#     "Choose course",
#     ["Report Generation in Streamlit", "Advanced Cryptography"],
#     index=0,
# )
# grade = form.slider("Grade", 1, 100, 60)
# submit = form.form_submit_button("Generate PDF")

# if submit:
#     html = template.render(
#         student=student,
#         course=course,
#         grade=f"{grade}/100",
#         date=date.today().strftime("%B %d, %Y"),
#     )

#     pdf = pdfkit.from_string(html, False)
#     st.balloons()

#     right.success("🎉 Your diploma was generated!")
#     # st.write(html, unsafe_allow_html=True)
#     # st.write("")
#     right.download_button(
#         "⬇️ Download PDF",
#         data=pdf,
#         file_name="diploma.pdf",
#         mime="application/octet-stream",
#     )
