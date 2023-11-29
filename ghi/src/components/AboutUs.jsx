import React from "react";
import "./AboutUs.css";

const AboutUs = () => {
  return (
    <div>
      <div className="page-header">
        <h1 className="title">ABOUT THE DEVELOPERS</h1>
      </div>
      <div className="about-us-container">
        <div className="about-us-header">Seth Porche from Tampa, FL</div>
        <div className="about-us-content">
          <p>
            "Hi, I'm Seth, a passionate individual with a diverse set of
            interests. When I'm not immersed in the world of coding, you'll find
            me crafting beats and melodies, diving into captivating video games,
            exploring the art of filmm, experimenting with new recipes in the
            kitchen, and getting lost in the pages of a good book. 💑 I've been
            happily married to my wonderful wife Kaley for two years, and we
            navigate the journey of life together. 📚 Currently on the verge of
            graduating, I'm eagerly gearing up to embark on a new adventure in
            the tech world. While my professional background has roots in
            logistics, where I managed a warehouse for a distribution company,
            my heart and future lie in software engineering. In early 2024, I'll
            be on the lookout for exciting opportunities to contribute my skills
            and passion to the world of technology."
          </p>
          {/* Add more content as needed */}
        </div>
      </div>
    </div>
  );
};

export default AboutUs;
